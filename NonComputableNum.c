/*
 * Problem from EPI[1]
 *
 * Given a set of coins (pennies, nickle, dimes or other denominations), find
 * the smallest number that cannot be constructed with provided coins. Note that
 * there can be many coins of each denomination. 
 *
 * Ex: int coins[] = {1,1,1,1,1,5,10,25}
 * Ans: 21
 *
 * [1] Elements of Programming Interviews, Page 32
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

/* Comparator to pass in to qsort() function */
int cmp(const void *a, const void *b) {
    return (*(int *)a - *(int *)b);
}

/* - Sort the input coins array
 * - Imagine an array M[] of same size as coins
 * - M[i] indicates maximum computable value at index/coin i
 * - Let coin[i] be denoted x
 * - If x > M[i-1]+1 then M[i-1]+1 is the first unreachable value
 * - If x <= M[i-1]+1 then M[i] = M[i-1]+x
 *      keep going till all coins are done
 *
 * - Note that there's no need to maintain M[] array. A single variable is
 *   enough
 *
 *   This algo runs in linear time (over number of coins). It also doesn't care
 *   if coins are duplicates. However, sorting will take O(N lnN), where N is
 *   number of coins.
 *
 *   TBD: Few corner cases must be considered. Will 'num' overflow?
 */
int firstNonComputableNum(int coins[], int sz) {
    int num = 0;

    for (int i=0; i<sz; i++) {
        if (coins[i] > num+1)   return num+1;
        num += coins[i];
    }

    return num+1;
}

int main(int argc, char *argv[]) {

    int S[128]; // max 128 numbers for now
    int sz=10;  // size of input

    srand(time(NULL));

    printf("Coins: ");
    for (int i=0; i<sz ; i++) {
        S[i] = rand()%10;
        printf("%d ", S[i]);
    }

    qsort(S, sz, sizeof(int), cmp);

    printf("\nSorted Coins: ");
    for (int i=0; i<sz ; i++) printf("%d ", S[i]);
    
    printf("\nFirst non computable number: %d\n", firstNonComputableNum(S, sz));


    return 0;
}
