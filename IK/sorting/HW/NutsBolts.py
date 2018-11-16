
def partition(arr, pivot, start, end):
    '''
    @param
    arr     array to partition
    pivot   well, pivot number
    start   start index within array
    end     end index, inclusive, within array
    @return
    returns position of pivot element, assuming it will be present in the array
    '''
    i = start
    j = end
    while True:
        while i <= j and arr[i] <= pivot: i += 1
        while i <= j and arr[j] > pivot: j -= 1

        if i > j: break

        arr[i], arr[j] = arr[j], arr[i]

    return j


def solve(nuts, bolts):

    pivot = nuts[0]
    start = 0
    end = len(nuts)-1

    for i in range(0, len(nuts)):
        pos = partition(bolts, pivot, start, end)
        pivot = nuts[pos]


if __name__ == "__main__":
    nuts = [4, 32, 5, 7]
    bolts = [32, 7, 5, 4]

    solve(nuts, bolts)
    print(nuts, bolts)
