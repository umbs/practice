from random import randint

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def get_pivot_index(start, end):
    '''
    start and end indices, are both inclusive
    '''
    return randint(start, end)


def partition(arr, start, end, p_idx):
    '''
    Use Lumoto's algorithm. When paritioning is done, swap element at 'end'
    where pivot is present with 'le'
      +----------+-+----------+-+--------------+-+
      |   <=     | |   >      | |    ??        | |
      +----------+-+----------+-+--------------+-+
                  ^            ^                      ^
                  le           cur                   end
    le = all elements less than or equal to pivot. It points to the next
         position an element must go if it is <= pivot
    cur = currently examining element
    start = Well, start of the array
    end = end of the array. This is the pivot element
    p_idx = Initially, pivot is here. Swap it to the end, to make it easy to
            partition.
    '''
    swap(arr, end, p_idx)
    le, cur, pivot = start, start, arr[end]

    while cur < end:
        if arr[cur] <= pivot:
            swap(arr, le, cur)
            le, cur = le+1, cur+1
        else:
            cur += 1

    swap(arr, le, cur)
    return le


def test_partition(arr, p_idx):
    '''
    Given pivot index, confirm that all values before it are less than or equal
    and all values later are greater than pivot
    '''
    for i in range(p_idx+1):
        if(arr[i] > arr[p_idx]):
            return False

    for i in range(p_idx+1, len(arr)):
        if(arr[i] <= arr[p_idx]):
            return False

    return True


def Quicksort(arr, start, end):
    if start >= end:
        return

    p_old = get_pivot_index(start, end)
    p_final = partition(arr, start, end, p_old)

    Quicksort(arr, start, p_final-1)
    Quicksort(arr, p_final+1, end)


def test_quicksort(arr):
    '''
    Test for ascending array
    '''
    for i in range(1, len(arr)):
        if arr[i-1] > arr[i]:
            return False

    return True
        

if __name__ == "__main__":
    for i in range(100):
        arr_sz = 100
        arr = [randint(-15, 15) for _ in range(arr_sz)]
        Quicksort(arr, 0, arr_sz-1)
        if not test_quicksort(arr):
            print("Quicksort Failed")
            print(arr)
            break
