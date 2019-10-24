
/* Grammar interface */

#ifndef Py_GRAMMAR_H
#define Py_GRAMMAR_H
#ifdef __cplusplus
extern "C" {
#endif

#include "bitset.h" /* Sigh... */

/* A label of an arc */

typedef struct {
    int          lb_type;
<<<<<<< HEAD
    char        *lb_str;
=======
    const char  *lb_str;
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
} label;

#define EMPTY 0         /* Label number 0 is by definition the empty label */

/* A list of labels */

typedef struct {
    int          ll_nlabels;
<<<<<<< HEAD
    label       *ll_label;
=======
    const label *ll_label;
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
} labellist;

/* An arc from one state to another */

typedef struct {
    short       a_lbl;          /* Label of this arc */
    short       a_arrow;        /* State where this arc goes to */
} arc;

/* A state in a DFA */

typedef struct {
    int          s_narcs;
<<<<<<< HEAD
    arc         *s_arc;         /* Array of arcs */
=======
    const arc   *s_arc;         /* Array of arcs */
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78

    /* Optional accelerators */
    int          s_lower;       /* Lowest label index */
    int          s_upper;       /* Highest label index */
    int         *s_accel;       /* Accelerator */
    int          s_accept;      /* Nonzero for accepting state */
} state;

/* A DFA */

typedef struct {
    int          d_type;        /* Non-terminal this represents */
    char        *d_name;        /* For printing */
<<<<<<< HEAD
    int          d_initial;     /* Initial state */
=======
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
    int          d_nstates;
    state       *d_state;       /* Array of states */
    bitset       d_first;
} dfa;

/* A grammar */

typedef struct {
    int          g_ndfas;
<<<<<<< HEAD
    dfa         *g_dfa;         /* Array of DFAs */
    labellist    g_ll;
=======
    const dfa   *g_dfa;         /* Array of DFAs */
    const labellist g_ll;
>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
    int          g_start;       /* Start symbol of the grammar */
    int          g_accel;       /* Set if accelerators present */
} grammar;

/* FUNCTIONS */
<<<<<<< HEAD

grammar *newgrammar(int start);
void freegrammar(grammar *g);
dfa *adddfa(grammar *g, int type, const char *name);
int addstate(dfa *d);
void addarc(dfa *d, int from, int to, int lbl);
dfa *PyGrammar_FindDFA(grammar *g, int type);

int addlabel(labellist *ll, int type, const char *str);
int findlabel(labellist *ll, int type, const char *str);
const char *PyGrammar_LabelRepr(label *lb);
void translatelabels(grammar *g);

void addfirstsets(grammar *g);

void PyGrammar_AddAccelerators(grammar *g);
void PyGrammar_RemoveAccelerators(grammar *);

void printgrammar(grammar *g, FILE *fp);
void printnonterminals(grammar *g, FILE *fp);

=======
const dfa *PyGrammar_FindDFA(grammar *g, int type);
const char *PyGrammar_LabelRepr(label *lb);
void PyGrammar_AddAccelerators(grammar *g);
void PyGrammar_RemoveAccelerators(grammar *);

>>>>>>> 716b15a33aed978ded8a6bde17855cb6c6aa7f78
#ifdef __cplusplus
}
#endif
#endif /* !Py_GRAMMAR_H */
