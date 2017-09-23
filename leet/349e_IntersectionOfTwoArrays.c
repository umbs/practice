int cmp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* intersection(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {

    #define n1 nums1Size
    #define n2 nums2Size
    #define rs returnSize

    int *result = malloc(sizeof(int) * (n1<n2?n1:n2));

    //check result is non NULL

    qsort(nums1, n1, sizeof(int), cmp);
    qsort(nums2, n2, sizeof(int), cmp);

    int i=0, j=0, k=0;
    int lastElem = nums1[0];

    while(i<n1 && j<n2) {
        if(nums1[i] < nums2[j])
            i++;
        else if(nums1[i] > nums2[j])
            j++;
        else {
            if(k==0 || result[k-1] != nums1[i]) {
                result[k] = nums1[i];
                k++;
            }
            i++; j++;
        }
    }

    *rs = k;

    return result;
}
