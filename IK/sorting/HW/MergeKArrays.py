from heapq import heappush, heappop

def mergeArrays(arr):
    K = len(arr)
    N = len(arr[0])

    heap = list()
    out = list()

    # initialize
    for i in range(K):
        heappush(heap, [arr[i][0], i, 0])


    while heap:
        elem, arr_num, idx = heappop(heap)
        out.append(elem)

        if idx+1 < len(arr[arr_num]):
            heappush(heap, [arr[arr_num][idx+1], arr_num, idx+1])

    return out


if __name__ == "__main__":
        # arr = [[1, 3, 5, 7], [2, 4, 6, 8], [0, 9, 10, 11]]
        arr = [[6, 10, 15], [7, 9, 18]]
        print(mergeArrays(arr))
