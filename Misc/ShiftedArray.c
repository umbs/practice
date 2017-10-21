#include <stdio.h>
#include <stdlib.h>


/*
 * Assumption: Sorted in ascending order. Elements are distinct.
 * Note: All elements in 1st half are greater than all elements in 2nd half
 *
 * Reference:
 * https://www.programcreek.com/2014/06/leetcode-search-in-rotated-sorted-array-java/
 */
int shiftedArrSearch(int *arr, size_t arrLen, int target)
{
  int lo = 0, hi = arrLen-1;

  while(lo<=hi) {
      int mid = lo + (hi-lo)/2;

      if(arr[mid] == target)
          return mid;

      // this range is monotonic (increasing)
      if(arr[lo]<=arr[mid]) {
          if(arr[lo]<=target && target<arr[mid])
              hi = mid-1;
          else
              lo = mid+1;
      } else {  // inflection happens in this range
          // (mid, hi) is monotonic range
          if(arr[mid]<target && target<=arr[hi])
              lo = mid+1;
          else
              hi = mid-1;
      }
  }

  return -1;
}

int main() {
  //int arr[] = {1, 2};
  int arr[] = {0, 1, 2, 3, 4, 5, 6, 7, 8};
  //int arr[] = {1, 2};
  //int arr[] = {1, 2};
  printf("%d \n", shiftedArrSearch(arr, 9, 2));
  return 0;
}
