/*
 * Problems from EPI[1]
 * 6.4 Given an array with values at i indicating how far to advance from i,
 * determine if end of the array can be reached from start.
 *
 * [1] Elements of Programming Interviews
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>
#include <stdbool.h>

#define MIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X, Y) ((X) < (Y) ? (Y) : (X))

void print(int *S, int sz) {
    for(int i=0; i<sz; i++) printf("%d ", S[i]);
    printf("\n");
}

bool canReachEnd(int *S, int sz) {
    int maxSoFar=0;
    for (int i=0; i<=maxSoFar && maxSoFar<sz; i++) {
        maxSoFar = MAX(maxSoFar, S[i]+i);
    }

    return (maxSoFar >= sz);
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

    for (int i=0; i<sz; i++)    S[i] = rand()%sz;
    print(S, sz);

    // function call goes here
    printf("Can reach end: %d\n", canReachEnd(S, sz));

    return 0;
}
