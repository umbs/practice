/* Dutch National Flag problem */
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

#define ELEM_SZ 10

int num[ELEM_SZ];

void fill() {
    for(int i=0; i<ELEM_SZ; i++) {
        num[i] = rand()%3;
    }
}

void print() {
    for(int i=0; i<ELEM_SZ; i++) {
        printf("%d ", num[i]);
    }
    printf("\n");
}

void exch(int i, int j) {
    if(i<0 || i>=ELEM_SZ)   return;
    if(j<0 || j>=ELEM_SZ)   return;

    int tmp = num[i];
    num[i] = num[j];
    num[j] = tmp;
}

void dnf() {
    int lo=0, lt=0, i=0;
    int gt=ELEM_SZ-1, hi=ELEM_SZ-1; // size of array

    while(i<=gt) {
        if(num[i] < 1)        exch(lt++, i++);
        else if(num[i] > 1)   exch(gt--, i);
        else                  i++;
    }
}

void main() {
    srand(time(NULL));
    fill();
    print();
    dnf();
    print();
}
