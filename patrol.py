import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python test_runner.py <path_to_patrol_executable>")
        sys.exit(1)

    patrol_path = sys.argv[1]

if __name__ == "__main__":
    main()
