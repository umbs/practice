int MAX(int x, int y) {
    return x > y ? x : y;
}

int cmp(const void *pa, const void *pb) {
    const int *a = *(const int **)pa;
    const int *b = *(const int **)pb;
    
    if(a[0] == b[0])    return a[1] - b[1];
    return a[0] - b[0];
}

// Let result[i] indicate longest chain for first i pairs
// Let (x,y) be the pair at index i
// Let gmax max chain length so far computed for index i
// result[i] = for each j from 0...i-1 and (a,b) be pair at j then
//                if(b < x) then 
//                    gmax = MAX(gmax, 1 + result[j])
int findLongestChain(int** pairs, int row, int col) {
    int *result = calloc(row, sizeof(int));
    
    for(int i=0; i<row; i++)
        result[i] = 1;
    
    qsort(pairs, row, sizeof pairs[0], cmp);

    int gmax = 1;   // result saved here
    for(int i=1; i<row; i++) {
        int lmax = 1;
        int x = pairs[i][0];
        
        for(int j=0; j<i; j++) {
            int b = pairs[j][1];
            
            if(b<x) {
                lmax = MAX(lmax, 1+result[j]);
            }
        }
        
        result[i] = lmax;
        gmax = MAX(gmax, lmax);
    }
    
    return gmax;
}
