/*
 * Problems from EPI[1]
 *
 * 6.2 Let an array represent an integer (positive). Write a func representing
 * that integer plus one. If the increment increases number of digits, resize
 * the array
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

void plusOne(int *A, int *sz) {
    if(sz == NULL || *sz == 0)  return;
    if(A == NULL)   return;

    int digits = *sz;
    int c=1;    // carry

    for(int i=digits-1; i>=0; i--) {
        A[i] += c;
        A[i] %= 10;
        c = (A[i] == 0);
    }

    if (c == 0) return;

    /* shift right if sum increased number of digits */
    A[0] = 1;
    for(int i=1; i<=*sz; i++)   A[i] = 0;
    *sz = *sz+1;

    print(A, *sz);
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

    for (int i=0; i<sz; i++)    S[i] = 8 + rand()%2;
    print(S, sz);

    // function call goes here
    plusOne(S, &sz);

    return 0;
}
