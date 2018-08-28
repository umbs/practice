import random

"""
  Quicksort
    - In Python, array size is inbuilt. But we do that here because on 
      recursive calls to same array, it indicates which portion of array the 
      sorting algorithm is examining/working on.
    - start, end are both inclusive
"""
def QuickSort(arr, start, end):
    if start >= end:
        return
    
    partition_index = Partition(arr, start, end)
    QuickSort(arr, start, partition_index-1)
    QuickSort(arr, partition_index+1, end)

def Partition(arr, start, end):
    pivot_element = arr[start]
    left = start + 1
    right = end
    
    while left <= right:
        while left <= right and arr[left] < pivot_element:
            left = left + 1
        while left <= right and arr[right] >= pivot_element:
            right = right - 1
        
        if left > right:
            break

        swap(arr, left, right)

    swap(arr, start, right)

    return right

"""
  Mergesort
    - start, end are inclusive 
"""
def mergesort(arr, start, end):
    if start >= end:
        return

    mid = start + (end - start)/2
    mergesort(arr, start, mid)
    mergesort(arr, mid+1, end)
    merge(arr, start, mid, end)


def merge(arr, start, mid, end):
    # do error checking
    result = []
    i = 0, j = 0, k = 0

    while i <
"""
  Generate arrays of random numbers of size N and within the range (0, limit),
  limit is inclusive
"""
def random_numbers(N, limit):
    arr = [random.randint(0, limit) for i in range(N)]
    return arr

def swap(arr, left, right):
    tmp = arr[left]
    arr[left] = arr[right]
    arr[right] = tmp



"""
  Testing Area 
"""

arr = random_numbers(25, 50)
print arr

QuickSort(arr, 0, len(arr)-1)
print arr
