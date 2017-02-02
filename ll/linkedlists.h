#include <stdio.h>
#include <stdlib.h>     //srand(), rand()
#include <limits.h>     // INT_MAX, UINT_MAX etc
#include <time.h>       // time()
#include <stdbool.h>    // _Bool, bool, true, false

#define MAX_LIST_SZ 100 // assume linked lists are sz 100, at most

/* Node in a linked list */
typedef struct _Node {
    int data;
    struct _Node *next;
} Node;

/* Node in a linked list */
typedef struct _rNode {
    int data;
    struct _rNode *rand;
    struct _rNode *next;
} rNode;

/* Node in a binary tree */
typedef struct _bNode {
    int data;
    struct _bNode *left;
    struct _bNode *right;
} bNode;

extern uint32_t hash(uint32_t a);
