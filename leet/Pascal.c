#include <stdio.h>
#include <stdlib.h>

/* Compute N'th row of a Pascal's triangle.
 * Rows of Pascal's triangle are binomial coefficients
 * Make use of this recursion.
 * C(n, k) = C(n, k-1) * (n-k+1)/k */
void pascal(int n) {
    int elem[256];  // max 256th row

    if(n>=256)  return;

    // initialize
    for(int i=0; i<256; i++)    elem[i] = 0;

    elem[0] = 1;

    for(int i=1; i<=n; i++) {
        elem[i] = elem[i-1] * (n-i+1)/i;
    }

    for(int i=0; i<=n; i++) {
        printf("%d ", elem[i]);
    }
    printf("\n");
}

int main() {
    pascal(6);
    return 0;
}
