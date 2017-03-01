/*
 * Problems from EPI[1]
 *
 * Template for Binary Trees (not BST). Careful, arrays are indexed from 1
 *
 * [1] Elements of Programming Interviews
 */
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

typedef struct _node {
    int data;
    int sz;     // num of nodes in subtree rooted at this node
    int level;  // height/level of this node from root. Root is at 0 level
    int lt, gt; // num of nodes whose data is less than (or gt) this node
    struct _node *l, *r, *p;    //l=left, r=right, p=parent
} Node;

void print(Node *S, int sz) {
    for(int i=1; i<=sz; i++) printf("%d ", S[i].data);
    printf("\n");
}

void inorder(Node *S) {
    if(S==NULL) return;

    inorder(S->l);
    printf("%d ", S->data);
    inorder(S->r);
}

void preorder(Node *S) {
    if(S==NULL) return;

    preorder(S->l);
    preorder(S->r);
    printf("%d ", S->data);
}

void postorder(Node *S) {
    if(S==NULL) return;

    printf("%d ", S->data);
    postorder(S->l);
    postorder(S->r);
}

bool isLeaf(Node *n) {
    if(n==NULL) return false;   // this is invalid arg
    return((n->l==NULL) && (n->r==NULL));
}

void buildTree(Node *S, int sz) {
    /* Build Tree */
    for(int i=1; i<=sz; i++) {
        S[i].data = rand()%100;
        S[i].l = S[i].r = S[i].p = NULL;

        /* parent/child pointers */
        if(2*i <= sz) {
            S[i].l = &S[2*i];
            S[2*i].p = &S[i];
        }

        if(2*i+1 <= sz) {
            S[i].r = &S[2*i+1];
            S[2*i+1].p = &S[i];
        }

        /* compute level */
        if(S[i].p)  S[i].level = 1+S[i].p->level;
        else    S[i].level = 0;
    }
}

int main(int argc, char *argv[]) {

    Node S[128];    // max 128 numbers of nodes
    int sz;         // num of nodes in tree

    if(argc != 2)  {
        printf("Need at least 2 args\n");
        return 1;
    }

    sz = atoi(argv[1]);
    srand(time(NULL));
    buildTree(S, sz);

    print(S, sz);

    return 0;
}
