/*
 * Problems from EPI[1]
 *
 * Delete duplicate elems in a sorted array (ascending)
 *
 * [1] Elements of Programming Interviews
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define MIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X, Y) ((X) < (Y) ? (Y) : (X))

void print(int *S, int sz) {
    for(int i=0; i<sz; i++) printf("%d ", S[i]);
    printf("\n");
}

/* Comparator to pass to qsort() */
int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

/* Delete duplicates in an array */
int dd(int *S, int sz) {
    int i, cur;

    for(i=1, cur=0; i<sz; i++) {
        if(S[cur] != S[i])  S[++cur] = S[i];
    }

    return cur+1;
}

int main(int argc, char *argv[]) {

    int S[128]; // max 128 numbers for now
    int sz;  // size of input

    if (argc != 2)  {
        printf("Need at least 2 args\n");
        return 1;
    }

    sz = atoi(argv[1]);

    srand(time(NULL));

    for (int i=0; i<sz; i++)    S[i] = rand()%10;
    print(S, sz);

    qsort(S, sz, sizeof(int), cmp);
    print(S, sz);

    // function call goes here
    int newSz = dd(S, sz);
    print(S, newSz);

    return 0;
}
