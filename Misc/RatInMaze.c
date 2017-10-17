#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define N 4

// return true if rat can reach destination.
// Source: (0,0); Destination: (N-1,N-1)
// A cell with 0 = dead end; with 1 = open
// Rat can move only right and down

bool sol[N][N];

bool solveMaze(int maze[N][N]) {
    for(int i=1; i<N; i++) {
        for(int j=1; j<N; j++) {
            if(maze[i][j] == 1) {
                sol[i][j] = sol[i-1][j] | sol[i][j-1];
            }
        }
    }

    return sol[N-1][N-1];
}

void main() {
    // Initialization
    for(int i=0; i<N; i++) {
        for(int j=0; j<N; j++) {
            sol[i][j] = false;
        }
    }

    int maze[N][N] = {{1, 0, 0, 0},
                    {1, 1, 0, 1},
                    {0, 1, 0, 0},
                    {1, 1, 1, 1},
                    };

    if(maze[0][0] == 0) return;
    else    sol[0][0] = true;

    // Initialization along top horizontal row
    for(int i=1; i<N; i++) {
        if(maze[i][0])
            sol[i][0] = sol[i-1][0];
    }

    // Initialization along first vertical column
    for(int i=1; i<N; i++) {
        if(maze[0][i])
            sol[0][i] = sol[0][i-1];
    }

    printf("%d \n", solveMaze(maze));
}
