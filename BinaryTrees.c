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

int main(int argc, char *argv[]) {

    Node S[128];    // max 128 numbers of nodes
    int sz;         // num of nodes in tree

    if(argc != 2)  {
        printf("Need at least 2 args\n");
        return 1;
    }

    sz = atoi(argv[1]);

    for(int i=1; i<=sz; i++) {
        S[i].data = rand()%100;
        S[i].l = S[i].r = S[i].p = NULL;

        if(2*i <= sz) {
            S[i].l = &S[2*i];
            S[2*i].p = &S[i];
        }

        if(2*i+1 <= sz) {
            S[i].r = &S[2*i+1];
            S[2*i+1].p = &S[i];
        }
    }

    print(S, sz);

    return 0;
}
