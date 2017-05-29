 #include <stdio.h>
 #include <stdlib.h>
 #include <limits.h>
 #include <time.h>
 
 // comparator function
 int cmp(const void *a, const void *b) {
     return ((Interval *)a->start - (Interval *)b->start);
 }
 
/**
 * Return an array of size *returnSize.
 * Note: The returned array must be malloced, assume caller calls free().
 */
struct Interval* merge(struct Interval* intervals, int intervalsSize, int* returnSize) {
    if(intervalsSize==0)    return NULL;
    if(intervalsSize==1)    return intervals;
    
    struct Interval *result = malloc(intervalsSize * sizeof(Interval));
    
    // Sort the input range, based on start value
    qsort(intervals, intervalsSize, sizeof(Interval), cmp);
    
    int i=0, j=0, k=0;
    
    for(i=0, j=0, k=0; i<intervalsSize;k++) {
        struct Interval intvl = {.start = 0, .end = 0};
        
        intvl.start = intervals[i].start;
        intvl.end = intervals[i].end;
        
        j = i+1;
        while(j<intervalsSize && intvl.end >= intervals[j].start) {
            intvl.end = intervals[j].end;
        }
        result[k].start = intvl.start;
        result[k].end   = intvl.end;
    }
    
    *returnSize = k;
    return result;
}
