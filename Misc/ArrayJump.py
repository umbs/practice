from random import randint
from time import time


def util(arr, visited, idx):
    if idx != len(arr)-1 and arr[idx] == 0:
        return False
    if idx == len(arr)-1:
        return True

    visited[idx] = True

    l = idx - arr[idx]
    r = idx + arr[idx]

    result = False

    if l >= 0 and not visited[l]:
        result |= util(arr, visited, l)
    if r <= len(arr)-1 and not visited[r]:
        result |= util(arr, visited, r)

    return result


def Jump(arr):
    visited = [False] * len(arr)
    return util(arr, visited, 0)


if __name__ == "__main__":
    # print(arr)
    # print(Jump(arr))
    start = time()
    for _ in xrange(1000000):
        arr = [randint(0, 2) for _ in range(10)]
        Jump(arr)
    end = time()
    print("Speed: " + str(end-start))
