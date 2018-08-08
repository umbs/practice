import random

def QuickSort(arr, start, end):
    if start >= end:
        return
    
    partition_index = Partition(arr, start, end)
    QuickSort(arr, start, partition_index-1)
    QuickSort(arr, partition_index+1, end)

def Swap(arr, left, right):
    tmp = arr[left]
    arr[left] = arr[right]
    arr[right] = tmp

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

        Swap(arr, left, right)

    Swap(arr, start, right)

    return right

def random_numbers(N, limit):
    arr = [random.randint(0, limit) for i in range(N)]
    return arr



#arr = [15, 20, 5, 2, 31, 44, 64, 4, 7, 18, 55]
#QuickSort(arr, 0, len(arr)-1)
#print arr

arr = random_numbers(25, 50)
print arr

QuickSort(arr, 0, len(arr)-1)
print arr
