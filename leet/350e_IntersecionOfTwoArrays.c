#include <stdio.h>
#include <stdlib.h>

int cmp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */

int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize) {

    #define n1 nums1Size
    #define n2 nums2Size
    #define rs returnSize

    int *result = malloc(sizeof(int) * (n1<n2?n1:n2));

    //check result is non NULL

    qsort(nums1, n1, sizeof(int), cmp);
    qsort(nums2, n2, sizeof(int), cmp);

    for(int i=0; i<n1; i++)
        printf("%d ", nums1[i]);
    printf("\n");

    for(int i=0; i<n2; i++)
        printf("%d ", nums2[i]);
    printf("\n");

    int i=0, j=0, k=0;

    while(i<n1 && j<n2) {
        if(nums1[i] < nums2[j])
            i++;
        else if(nums1[i] > nums2[j])
            j++;
        else {
            result[k] = nums1[i];
            i++; j++; k++;
        }
    }

    *rs = k;

    return result;
}

void main() {
   int num1[] = {-2147483648,1,2,3};
   int num2[] = {1,-2147483648,-2147483648};

   int rs; 
   int *result = intersect(num1, 4, num2, 3, &rs);

   for(int i=0; i<rs; i++) {
       printf("%d ", result[i]);
   }
   printf("\n");
}
