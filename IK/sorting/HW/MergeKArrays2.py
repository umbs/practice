from heapq import heappush, heappop

'''
Initially, take all the first elements from all arrays and put them in min heap.

Then, keep pop'ing element out of heap and add them to resultant array. As we
pop, add next element from array (to which element belongs) to heap
'''

'''
arr is list of lists
'''
def mergeArrays(arr):
    heap = list()
    res = list()

    K = len(arr)    # number of arrays
    N = len(arr[0]) # number of elements in each array

    # Initialization
    # Each item contains following: [element, array number, index]
    for i in range(K):
        heappush(heap, [arr[i][0], i, 0])

    # Start pulling elem from heap and add it to result array
    while heap:
        elem, arr_num, idx = heappop(heap)
        res.append(elem)

        if idx+1 < len(arr[arr_num]):
            heappush(heap, [arr[arr_num][idx+1], arr_num, idx+1])

    return res

if __name__ == "__main__":
        arr = [[1, 3, 5, 7], [1, 3, 6, 8], [0, 9, 10, 11]]
        # arr = [[6, 10, 15], [7, 9, 18]]
        print(mergeArrays(arr))
