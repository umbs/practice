/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* countBits(int num, int* returnSize) {
    int *result = calloc(num+1, sizeof(int));
    
    int pow = 1;    // power of 2
    while(pow<num) {
        result[pow] = 1;
        pow *= 2;
    }
    
    int pow = 2;    // power of 2
    for(int i=3; i<=num; i++) {
        if(result[i] == 1) {
            pow = i;
            continue;
        }
        result[i] = 1 + result[i-pow];
    }
    
    *returnSize = num+1;
    
    return result;
}
