/*
 * Problems from EPI[1]
 * 
 * Given some plays (2, 3, 7 points of scores in each play), calculate number of
 * ways a final score can be acheived (here it's 12).
 *
 * DP 17.1
 *
 * [1] Elements of Programming Interviews
 */

#include <stdio.h>
#include <stdlib.h>
#include <limits.h>
#include <time.h>

int main(int argc, char *argv[]) {

    int numPlays = 3;
    int plays[] = {1, 2, 3};
    int finalScore = 4;
    int A[numPlays][finalScore+1];

    // initialize score 0 to 1. All others 0.
    for (int i=0; i<3; i++) {
        A[i][0] = 1;
        for (int j=1; j<=finalScore; j++)
            A[i][j] = 0;
    }

    // first play
    for (int j=1; j<=finalScore; j++)
        if (j%plays[0] == 0)
            A[0][j] = 1;

    // 2nd and subsequent plays
    for (int i=1; i<3; i++) {
        for (int j=1; j<=finalScore; j++) {
            A[i][j] = A[i-1][j];

            for (int k=1; k*plays[i]<=j; k++) {
                int score = k*plays[i];
                if (A[i-1][j-score]) A[i][j] += A[i-1][j-score];
            }
        }
    }

    // print
    for (int i=0; i<3; i++) {
        for (int j=0; j<=finalScore; j++) {
            printf("%d ", A[i][j]);
        }
        printf("\n");
    }

    return 0;
}
