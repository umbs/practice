#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void swap(int *arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

void print(int *arr, int lo, int hi) {
    if(arr == NULL) return;
    
    for(int i=lo; i<=hi; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

int *newArray(int sz) {
    int *arr = calloc(sz, sizeof(int)); // init to 0
    return arr; // caller checks for NULL
}

/* lo and hi inclusive */
void Quicksort(int *arr, int lo, int hi) {
    if(arr == NULL) return;
    if(lo >= hi)    return;

    int pivot = arr[lo];
    int i=lo+1, j=hi;

    while(i<j) {
        while(arr[i] < pivot)   i++;
        while(arr[j] >= pivot)  j--;

        if(i>=j)    break;

        swap(arr, i, j);
    }

    // swap pivot with jth element
    swap(arr, lo, j);

    Quicksort(arr, lo, j-1);
    Quicksort(arr, j+1, hi);    
}

int median(int *arr, int lo, int hi, int mid) {
    if(arr == NULL)
        return -1;
    if(lo==mid || hi==mid)  
        return arr[mid];
    if(lo >= hi)        
        return arr[hi];

    printf("lo: %d, hi: %d, mid: %d\n", lo, hi, mid);
    
    int pivot = arr[lo];
    int i=lo+1, j=hi;

    while(i<j) {
        while(i<j && arr[i] < pivot)   i++;
        while(i<j && arr[j] >= pivot)  j--;

        if(i>=j)    break;

        swap(arr, i, j);
    }

    // swap pivot with jth element
    // jth position is fixed.
    swap(arr, lo, j);

    if(j > mid) {
        return median(arr, lo, j-1, mid);
    } else if(j < mid) {
        return median(arr, j+1, hi, mid);
    } 
    
    return arr[j];
}

void main() {

#define SZ 10
#define RANGE 15

    int *arr = newArray(SZ);
    if(arr == NULL)     exit(EXIT_SUCCESS); // malloc failed

    srand(time(NULL));

    for(int i=0; i<SZ; i++) {
        arr[i] = rand()%RANGE;
    }

    print(arr, 0, SZ-1);
    Quicksort(arr, 0, SZ-1); 
}
