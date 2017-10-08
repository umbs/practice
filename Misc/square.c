#include <stdio.h>
#include <math.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// let bool canIWin[] indicate all the numbers from which a player can win. If
// canIWin[i] = 1 -> player can win
// canIWin[i] = 0 -> No way for a player to win
//
int getSquare(int score) {
    int canIWin[score+1];
    memset(canIWin, 0, sizeof(int) * (score+1));
    canIWin[1] = 1;

    // Build up the array until 'score'.
    // For a number i, check all perfect squares that can be removed so that
    // opponent can NEVER win (ie., canIWin[his score] = 0
    for(int i=2; i<=score; i++) {
        int subSquare = (int)sqrt((double) i);

        for(int j=1; j<=subSquare; j++) {
            if(canIWin[i-j*j] == 0) {
                canIWin[i] = 1;
                printf("Score %d, Square to remove: %d\n", i, j*j);
                break;
            }
        }
    }

    printf("Score: %d, %s\n", score, canIWin[score] ? "Win" : "Loose");
    return -1;
}

void main() {
    //getSquare(2);
    //getSquare(4);
    //getSquare(8);
    getSquare(14);
    //getSquare(50);
}
