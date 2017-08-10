
typedef struct {
    int num;    /* Key to hash */
    int idx;
    UT_hash_handle hh;
} numIdx;

numIdx *indices = NULL;

/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
int* nextGreaterElement(int* findNums, int findNumsSize, int* nums, int numsSize, int* returnSize) {
    if(findNumsSize == 0 || numsSize == 0)   return NULL;

    int *nge = malloc(findNumsSize);

    /* Initialize */
    for(int i=0; i<findNumsSize; i++)   
        nge[i] = -1;

    /* Build the hash */
    for(int i=0; i<numsSize; i++) {
        numIdx *a = malloc(sizeof *a);
        a->num = nums[i];
        a->idx = i;

        HASH_ADD_INT(indices, num, a);
    }

    /* */
    for(int i=0; i<findNumsSize; i++) {
        numIdx *a;
        HASH_FIND_INT(indices, &findNums[i], a);

        /* Should NOT happen */
        if(a==NULL) {
            return NULL;
        }

        /* find Greater element */
        for(int k=a->idx+1; k<numsSize; k++) {
            if(findNums[i] >= nums[k])  continue;

            nge[i] = nums[k];
            break;
        }
    }

    *returnSize = findNumsSize;

    return nge;
}
