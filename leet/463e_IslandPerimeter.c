int islandPerimeter(int** grid, int gridRowSize, int gridColSize) {

#define row gridRowSize
#define col gridColSize

    int peri = 0;
    for(int i=0; i<row; i++) {
        for(int j=0; j<col; j++) {
            if(grid[i][j]==0)   continue;
            
            int cir = 4;
            if(i>0 && grid[i-1][j])     cir--;
            if(i+1<row && grid[i+1][j]) cir--;
            if(j>0 && grid[i][j-1])     cir--;
            if(j+1<col && grid[i][j+1]) cir--;

            peri += cir;
        }
    }

    return peri;
}
