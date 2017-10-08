#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#define ROW 5
#define COL 5

bool canVisit(int arr[][COL], int row, int col, bool visited[][COL]) {
    return (row>=0 && row < ROW) && (col>=0 && col<COL) && arr[row][col] && !visited[row][col];
}

// DFS search once a cell with 1 is hit
void DFS(int arr[][COL], int row, int col, bool visited[][COL]) {
    // arrays to get to 8 neighbors
    static int rowNbr[] = {-1, -1, -1, 0, 0, 1, 1, 1};
    static int colNbr[] = {-1, 0, 1, -1, 1, -1, 0, 1};

    visited[row][col] = true;

    // visit all 8 cells
    for(int i=0; i<8; i++) {

        int r = row+rowNbr[i];
        int c = col+colNbr[i];

        if(canVisit(arr, r, c, visited)) {
            DFS(arr, r, c, visited);
        }
    }
}

int countIslands(int arr[ROW][COL]) {
    bool visited[ROW][COL];
    memset(visited, 0, sizeof(visited));

    int count = 0;
    for(int i=0; i<ROW; i++) {
        for(int j=0; j<COL; j++) {
            if(arr[i][j] && !visited[i][j]) {
                DFS(arr, i, j, visited);
                count++;
            }
        }
    }

    return count;
}


void main() {
    int M[][COL]= {  {1, 1, 0, 0, 0},
        {0, 1, 0, 0, 1},
        {1, 0, 0, 1, 1},
        {0, 0, 0, 0, 0},
        {1, 0, 1, 0, 1}
    };

    printf("Number of islands is: %d\n", countIslands(M));
}
