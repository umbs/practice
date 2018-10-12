import heapq
import random


def topK(arr, k):
    if k <= 0 or not arr:
        print("Invalid input")
        return

    H = [arr[0]]
    S = {arr[0]}

    for e in arr:
        if e in S:
            continue

        if len(H) < k:
            heapq.heappush(H, e)
        elif H[0] < e:
            heapq.heapreplace(H, e)

        S.add(e)

    return H


if __name__ == "__main__":

    arr = [random.randint(-10, 10) for _ in range(10)]
    k = 3

    print(sorted(arr))
    print(topK(arr, k))
