#ifndef BYTEBOX_FORGE_H_INCLUDED
#define BYTEBOX_FORGE_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

enum bbcode {
    BB_OK = 0,
    BB_ERR_MAX
};

struct bbforge;
struct bbstatus;

struct bbforge *new_forge(void);
void del_forge(struct bbforge *me);
enum bbcode forge_craft(struct bbforge *me, const char *fname);
struct bbstatus *forge_status(struct bbforge *me);

#ifdef __cplusplus
}
#endif

#endif /* BYTEBOX_FORGE_H_INCLUDED */
