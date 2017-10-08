#include <stdio.h>
#include <stdlib.h>

int main() {
    //int arr[] = {10, 2, 4, 5, 9};
    int arr[] = {1, 100, 2, 3, 101, 5, 103};
    int sz = sizeof(arr)/sizeof(arr[0]);
    int maxLis=1, lis=1;

    if(sz==1)   return maxLis;

    int prev = arr[0];

    for(int i=1; i<sz; i++) {
        if(arr[i] > prev)   lis++;
        else    lis = 1;

        if(lis>maxLis)  maxLis = lis;
    }

    printf("maxLis: %d\n", maxLis);

    return 0;
}
