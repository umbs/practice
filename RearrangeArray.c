/*
 * Problem from EPI[1]
 *
 * Given an array of ints, say, rearrange it's elements to satisfy following:
 *
 *   A[0] <= A[1] >= A[2] <= A[3] >= A[4] <= ...
 *
 * [1] Elements of Programming Interviews, Page 32
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

void swap(int A[], int i, int j) {
    int t = A[i];
    A[i] = A[j];
    A[j] = t;
}

/* Linear run time */
void rearrange(int A[], int sz) {
    for (int i=0; i<sz-1; i++) {
        if ((i%2 == 0 && A[i]>A[i+1]) ||
                (i%2 == 1 && A[i]<=A[i+1]))
            swap(A, i, i+1);
    }
}

int main(int argc, char *argv[]) {

    int S[128]; // max 128 numbers for now
    int sz=10;  // size of input

    srand(time(NULL));

    printf("Array: ");
    for (int i=0; i<sz ; i++) {
        S[i] = rand()%100;
        printf("%d ", S[i]);
    }

    rearrange(S, sz);

    printf("\nRearranged Array: ");
    for (int i=0; i<sz ; i++) printf("%d ", S[i]);
    printf("\n");

    return 0;
}
