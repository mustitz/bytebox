#ifndef BYTEBOX_CHRONICLE_H_INCLUDED
#define BYTEBOX_CHRONICLE_H_INCLUDED

#include <stdint.h>

#include "bytebox/dlist.h"

#ifdef __cplusplus
extern "C" {
#endif

enum bburgency {
    BB_TRACE = 0,
    BB_DEBUG,
    BB_INFO,
    BB_WARN,
    BB_ERROR,
    BB_MAX_URGENCY
};

enum bbchronicle_opts {
    BBCHRONICLE_LAST_ONLY = 1,
    BBCHRONICLE_AUTO_PRINT = 2,
    BBCHRONICLE_ALL = 3
};

struct bbpos {
    const char * file;
    const char * func;
    int line;
};

struct bbreadout {
    uint64_t ts;
    int pid;
    int tid;
};

struct bbfact {
    enum bburgency level;
    const char * message;
    struct bbreadout readout;
    struct bbpos pos;
    struct dlist link;
    void * supplement;
};

struct bbreport {
    const char * api;
    struct dlist facts;
    int64_t ns_duration;
    struct dlist link;
};

struct bbchronicle {
    struct dlist reports;
    int flags;
};

struct bbchronicle * new_chronicle(int options);
void del_chronicle(struct bbchronicle * me);

#ifdef __cplusplus
}
#endif

#endif /* BYTEBOX_CHRONICLE_H_INCLUDED */
