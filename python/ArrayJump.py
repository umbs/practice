"""
Problem Description:

    Advancing through an array: Given an array of integers, representing how far
    can you jump from that index, determine if you can reach the end from start.

    Variant: Minimum jumps to reach the end.

Example:
    arr = [1, 0, 4, 3, 2, 2, 0, 1]

Solution/Algorithm:
Pseudocode:
    for i in range and i <= furthest:
        furthest = max(furthest, i + arr[i])

    if i > furthest:
        return False

    return True
"""

import random

def make_array(arr, lo, hi, size):
    for i in range(size):
        arr.append(random.randint(lo, hi))

def array_jump(arr):
    far = 0
    i = 0
    lastIndex = len(arr)
    while i < lastIndex and i <= far:
        far = max(far, i + arr[i])

        # it's possible to reach end, not required to search further
        if far >= lastIndex:
            return True

        i += 1

    if i == lastIndex:
        return True

    print i, lastIndex, far

    return False

if __name__ == "__main__":
    #arr = random.sample(xrange(1, 3), 10)

    arr = []
    make_array(arr, 0, 2, 10)
    print arr
    print array_jump(arr)
