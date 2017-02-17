/*
 * Problems from EPI[1]
 *
 * Dutch National Flag problem. Given an array and a pivot element (within an
 * array), rearrange elements such that all elements less than pivot is at
 * start, then equal elems and then larger elems.
 *
 * [1] Elements of Programming Interviews
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

void print(int *S, int sz) {
    for(int i=0; i<sz; i++) printf("%d ", S[i]);
    printf("\n");
}

void swap(int *S, int i, int j) {
    int temp = S[i];
    S[i] = S[j];
    S[j] = temp;
}

/* Dutch National Flag. Used Quicksort's 3-way partition solution from Bob
 * Sedgewick's course
 *
 *  http://algs4.cs.princeton.edu/23quicksort/
 *  http://algs4.cs.princeton.edu/23quicksort/Quick3way.java.html
 *
 *         1               2              3              4
 *   +----------------------------------------------------------+
 *   |    < piv     |     = piv    |     ???      |     > piv   |
 *   +----------------------------------------------------------+
 *   ^              ^              ^              ^             ^
 *   lo             lt             i              gt            hi
 *
 * */
void dnf(int *S, int sz, int p) {

    if(sz==0 || sz==1) return;  // nothing to do
    if(p>=sz)   return;         // invalid pivot
    if(S==NULL) return;         // invalid args

    int piv = S[p];     // pivot
    int lo=0, hi=sz-1, lt=lo, gt=hi, i=lo;

    while(i <= gt) {
        // put in subarray 1
        if(S[i]<piv) {
            swap(S, lt, i);
            lt++; i++;
        }
        // put in subarray 4
        else if(S[i]>piv) {
            swap(S, i, gt);
            gt--;
        }
        // leave elem in subarray 3
        else {
            i++;
        }
    }

    print(S, sz);
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

    for (int i=0; i<sz; i++)    S[i] = rand()%2;
    print(S, sz);

    // function call goes here
    dnf(S, sz, 0);

    return 0;
}
