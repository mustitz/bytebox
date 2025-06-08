#ifndef BYTEBOX_DLIST_H_INCLUDED
#define BYTEBOX_DLIST_H_INCLUDED

#ifdef __cplusplus
extern "C" {
#endif

/*
 * Double linked lists.
 */

struct dlist
{
    struct dlist *next;
    struct dlist *prev;
};

static inline void dlist_init(struct dlist *me)
{
    me->next = me;
    me->prev = me;
}

static inline void dlist_insert_after(struct dlist *prev, struct dlist *infant)
{
    struct dlist * next = prev->next;
    infant->next = next;
    infant->prev = prev;
    next->prev = infant;
    prev->next = infant;
};

static inline void dlist_insert_before(struct dlist *next, struct dlist *infant)
{
    dlist_insert_after(next->prev, infant);
}

static inline void dlist_remove(struct dlist *item)
{
    item->prev->next = item->next;
    item->next->prev = item->prev;
}

#ifdef __cplusplus
}
#endif

#endif /* BYTEBOX_DLIST_H_INCLUDED */
