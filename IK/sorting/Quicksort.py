import random

def pivot(arr, start, end):
    '''
    returns index of a pivot element. Assumes valid start and end
    '''
    return start


def partition(arr, idx, start, end):
    '''
    Given index of partition, rearrange elements and return final position of
    pivot
    '''
    l = start
    r = end

    while True:
        while l <= r and arr[l] <= arr[idx]: l += 1
        while l <= r and arr[r] > arr[idx]: r -= 1

        if l > r:
            break
        else:
            arr[l], arr[r] = arr[r], arr[l]

    arr[idx], arr[r] = arr[r], arr[idx]
    return r


def k_small(arr, k, start, end):
    if start >= end:
        return arr[start]

    idx = pivot(arr, start, end)
    pos = partition(arr, idx, start, end)

    if pos == (k-1):
        return arr[pos]

    if pos < (k-1):
        return k_small(arr, k, pos+1, end)
    else:
        return k_small(arr, k, start, pos-1)


def k_smallest(arr, k):
    return k_small(arr, k, 0, len(arr)-1)


if __name__ == "__main__":
    # arr = [3, 1, 0, 9, 7, 4]
    for i in range(1, 1000):
        arr = [random.randint(1, 100) for _ in range(25)]
        # print sorted(arr)
        print k_smallest(arr, 5)
