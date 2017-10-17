#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>


/*
N(i,j) = Number of ways of reaching position (i,j) for valid i and j and staying in same search half
       = N(i-1,j) + N(i, j-1)
       
 Initial conditions, N(0,j) = 1 and N(i, 0) = 1 for all i and j
*/

int N[101][101];  // global, initialized to 0

int helper(int n) {
    for(int i=1; i<n; i++) {
        for(int j=1; j<n; j++) {

            if(j>i) {
                break;
            }

            if(i == j)  N[i][j] = N[i][j-1];
            else        N[i][j] = N[i-1][j] + N[i][j-1];
        }
    }

    return N[n-1][n-1];
}

int numOfPathsToDest(int n) 
{
    printf("n=%d: ", n);
    if(n==0 || n==1)  return n;

    for(int i=0; i<n; i++)
        N[0][i] = 1;

    for(int j=0; j<n; j++)
        N[j][0] = 1;

    // your code goes here
    return helper(n);
}

int main() {
    for(int i=0; i<10; i++) {
        printf("%d\n", numOfPathsToDest(i));
    }
    printf("\n");

    return 0;
}
