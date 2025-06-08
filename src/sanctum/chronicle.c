#include <stdlib.h>
#include "bytebox/chronicle.h"

struct bbchronicle * new_chronicle(int options)
{
    struct bbchronicle * chronicle = malloc(sizeof(struct bbchronicle));
    if (chronicle == NULL) {
        return NULL;
    }

    dlist_init(&chronicle->reports);
    chronicle->flags = options;
    return chronicle;
}

void del_chronicle(struct bbchronicle * me)
{
    if (me == NULL) {
        return;
    }

    free(me);
}
