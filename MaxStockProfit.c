/*
 * Problem from EPI[1]
 *
 * Given a history of stocks each day going back to past N days, user can only
 * buy/sell stock at start of day. Determine their max profit.
 *
 * [1] Elements of Programming Interviews, Page 2
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

#define MIN(X, Y) ((X) < (Y) ? (X) : (Y))
#define MAX(X, Y) ((X) < (Y) ? (Y) : (X))

/*
 * This is a O(N) run time and O(1) space algo. The *trick* here is maxProfit is
 * independent of current minPrice. maxProfit is computed in single pass.
 */
int getMaxProfit(int S[], int sz) {
    int maxProfit = 0, minPrice = INT_MAX;

    for (int i=0; i<sz; i++) {
        minPrice = MIN(S[i], minPrice);
        maxProfit = MAX(maxProfit, S[i]-minPrice);
    }

    return maxProfit;
}

int main(int argc, char *argv[]) {

    int S[128]; // max 128 numbers for now
    int sz=10;  // size of input

    srand(time(NULL));

    for (int i=0; i<sz ; i++) {
        S[i] = rand()%100;
        printf("%d ", S[i]);
    }

    printf("Max Profit: %d\n", getMaxProfit(S, sz));

    return 0;
}
