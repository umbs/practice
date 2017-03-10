/*
 * Move all even numbers to front and odd to back of a given array
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

void swap(int a[], int i, int j) {
    int temp = a[i];
    a[i] = a[j];
    a[j] = temp;
}

void evenOdd(int a[], int sz) {
    int e=0, o=sz-1;

    while (e<o) {
        while (a[e]%2==0 && e<o)  e++;
        while (a[o]%2==1 && e<o)  o--;

        if (e >= o) return;

        swap(a, e, o);
    }
}

int main(int argc, char *argv[]) {

    int S[128]; // max 128 numbers for now
    int sz=10;  // size of input

    srand(time(NULL));

    for (int i=0; i<sz ; i++) {
        S[i] = rand()%100;
        printf("%d ", S[i]);
    }

    evenOdd(S, sz);
    printf("\n");

    for (int i=0; i<sz ; i++) {
        printf("%d ", S[i]);
    }

    printf("\n");

    return 0;
}
