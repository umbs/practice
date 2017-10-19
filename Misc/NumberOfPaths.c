#include <stdio.h>

int a[101][101];

int numOfPathsToDest(int N) {
    for(int i=0; i<N; i++)
        a[i][0] = 1;

    for(int i=0; i<N; i++)
        a[N-1][i] = 1;

    for(int i=1; i<N; i++) {
        for(int j=1; j<=i; j++) {
            if(i==j)    a[i][j] = a[i][j-1];
            else        a[i][j] = a[i][j-1] + a[i-1][j];
        }
    }

    return a[N-1][N-1];
}

void main() {
    for(int i=1; i<=7; i++) {
        printf("(%d, %d)\n", i, numOfPathsToDest(i));
    }
}
