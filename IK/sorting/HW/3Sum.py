import sys

def findPairAddsToK(arr, K, start, end):
    '''
    Find list of paoirs in arr that add up to K. Assume that array is sorted
    in ascending order. start and end are inclusive indices within arr that
    must be examined
    '''

    res = []
    i = start
    j = end
    while i < j:
        add = arr[i] + arr[j]
        if add == K:
            res.append([arr[i], arr[j]])
            i, j = i+1, j-1

            # Skip duplicate numbers
            while i < j and arr[i] == arr[i-1]:
                i += 1
            while i < j and arr[j] == arr[j+1]:
                j -= 1

        elif add < K:
            i += 1
        elif add > K:
            j -= 1
    return res


def findZeroSum(arr):
    '''
    Given an array of ints, return all triplets that sum to zero
    '''
    arr.sort()
    sz = len(arr)

    res = []

    for i in range(sz):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        pairs = findPairAddsToK(arr, -arr[i], i+1, sz-1)
        for p in pairs:
            triplet = [arr[i]]
            triplet.extend(p)
            res.append(triplet)

    result = [','.join(str(e) for e in r) for r in res]

    return result


if __name__ == "__main__":
    f = sys.stdout

    arr_size = int(input())

    arr = []
    for _ in range(arr_size):
        arr_item = int(input())
        arr.append(arr_item)

    res = findZeroSum(arr)

    f.write("\n".join(res))

    f.write('\n')

    f.close()
