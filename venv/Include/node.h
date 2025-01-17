
/* Parse tree node interface */

#ifndef Py_NODE_H
#define Py_NODE_H
#ifdef __cplusplus
extern "C" {
#endif

typedef struct _node {
    short               n_type;
    char                *n_str;
    int                 n_lineno;
    int                 n_col_offset;
    int                 n_nchildren;
    struct _node        *n_child;
<<<<<<< HEAD
=======
    int                 n_end_lineno;
    int                 n_end_col_offset;
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
} node;

PyAPI_FUNC(node *) PyNode_New(int type);
PyAPI_FUNC(int) PyNode_AddChild(node *n, int type,
<<<<<<< HEAD
                                      char *str, int lineno, int col_offset);
=======
                                char *str, int lineno, int col_offset,
                                int end_lineno, int end_col_offset);
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
PyAPI_FUNC(void) PyNode_Free(node *n);
#ifndef Py_LIMITED_API
PyAPI_FUNC(Py_ssize_t) _PyNode_SizeOf(node *n);
#endif

/* Node access functions */
#define NCH(n)          ((n)->n_nchildren)

#define CHILD(n, i)     (&(n)->n_child[i])
#define RCHILD(n, i)    (CHILD(n, NCH(n) + i))
#define TYPE(n)         ((n)->n_type)
#define STR(n)          ((n)->n_str)
#define LINENO(n)       ((n)->n_lineno)

/* Assert that the type of a node is what we expect */
#define REQ(n, type) assert(TYPE(n) == (type))

PyAPI_FUNC(void) PyNode_ListTree(node *);
<<<<<<< HEAD
=======
void _PyNode_FinalizeEndPos(node *n);  // helper also used in parsetok.c
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78

#ifdef __cplusplus
}
#endif
#endif /* !Py_NODE_H */
