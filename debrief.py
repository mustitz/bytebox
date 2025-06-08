import subprocess
import sys

from datetime import datetime
from pathlib import Path
from time import time

def help(msg=None):
    print("🎖️ ByteBox Debrief - Mission Command System")
    print()
    if msg is not None:
        cmd = ' '.join(sys.argv)
        print(f"ERROR: {msg} in")
        print(f"  {cmd}")
        print()
    print("USAGE:")
    print("  python3 debrief.py <command> [args...]")
    print()
    print("COMMANDS:")
    print("  enter <builddir> <target>  - Execute enter-mission briefing")
    print("  leave <builddir> <target>  - Execute post-mission debrief")
    print("  run <patrol>    - Execute patrol mission")
    print("  help                       - Show this help")
    print()
    print("EXAMPLES:")
    print("  python3 debrief.py enter ./build check")
    print("  python3 debrief.py leave ./build check-asan")
    print("  python3 debrief.py run   ./build/check/sanctum-patrol")

def get_san(target):
    if not target.startswith("check"):
        raise ValueError(f"Target must be started from 'check', got {target}")

    if target == "check":
        return None

    if not target.startswith("check-"):
        ValueError(f"Target must be 'check' or 'check-<name>', got: {target}")

    _, name = target.split('-', maxsplit=1)
    return name

def get_check_stack_fn(builddir, target):
    dn = Path(builddir) / "tmp"

    name = get_san(target)
    if name is not None:
        dn /= name

    dn /= "recon"
    dn.mkdir(parents=True, exist_ok=True)

    srcroot = Path(__file__).parent
    cwdrel = str(Path.cwd().relative_to(srcroot)).replace('/', '.')
    return dn / (target if cwdrel == '.' else f"{cwdrel}.{target}")

def enter(builddir, target):
    get_check_stack_fn(builddir, target).touch()
    return 0

def aar():
    print("Not implemented: aar")
    return 1

def leave(builddir, target):
    fn = get_check_stack_fn(builddir, target)
    dn = fn.parent
    topfn = '.'.join(fn.name.split('.')[1:])
    if topfn:
        return aar()

    if (dn / topfn).exists():
        return 0

    return aar()

def launch(name, patrol, dn):
    dn.mkdir(parents=True, exist_ok=True)
    command = [patrol]
    timestamp = datetime.utcnow().strftime('%Y-%m-%dT%H:%M:%SZ')

    start = time()
    process = subprocess.Popen(
        command,
        cwd=dn,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    pid = process.pid if hasattr(process, 'pid') else '???'
    stdout, stderr = process.communicate()
    duration = time() - start

    params = {
        "EXITCODE": process.returncode,
        "TIMESTAMP": timestamp,
        "DURATION": f'{duration:.3f}',
        "COMMAND": [str(s) for s in command],
        "WORKDIR": dn,
        "PID": pid,
    }

    lines = []
    for key, value in params.items():
        lines.append(f"{key}: {value}")

    lines.append("--- STDOUT ---")
    if stdout:
        lines.append(stdout)
    lines.append("--- STDERR ---")
    if stderr:
        lines.append(stderr)
    lines.append("--- END ---\n")

    (dn / f'{name}.debrief.txt').write_text('\n'.join(lines))
    return 0

def run(patrol):
    patrol = Path(patrol)

    dn = patrol.parent
    while True:
        name = dn.name
        if name == 'check':
            break
        dn = dn.parent
        if dn == dn.parent:  # reached root
            raise ValueError(f"Could not find 'check' directory in patrol path: {patrol}")

    dn = dn.parent / "recon"

    parts = patrol.name.split('-')
    if parts[-1] != 'patrol':
        raise ValueError(f"Patrol executable should end with '-patrol': {patrol_name}")

    return launch('-'.join(parts[:-1]), patrol, dn)

def main():
    if len(sys.argv) < 2:
        help("No arguments provided")
        sys.exit(1)

    command = sys.argv[1]

    if command == "help":
        help()
        return 0

    if command == "enter":
        if len(sys.argv) != 4:
            help("enter command requires exactly 2 arguments: <builddir> <target>")
            sys.exit(1)
        builddir = sys.argv[2]
        target = sys.argv[3]
        return enter(builddir, target)

    if command == "leave":
        if len(sys.argv) != 4:
            help("leave command requires exactly 2 arguments: <builddir> <target>")
            sys.exit(1)
        builddir = sys.argv[2]
        target = sys.argv[3]
        return leave(builddir, target)

    if command == "run":
        if len(sys.argv) != 3:
            help("run command requires exactly 1 argument: <patrol>")
            sys.exit(1)
        patrol = sys.argv[2]
        return run(patrol)

    help(f"Unknown command: {command}")
    return 1

if __name__ == "__main__":
    sys.exit(main())
