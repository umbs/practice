def merger_first_into_second(a, b):
    i, j = len(a)-1, len(a)-1
    k = len(b)-1

    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            b[k] = a[i]
            i, k = i-1, k-1
        elif b[j] > a[i]:
            b[k] = b[j]
            j, k = j-1, k-1
        else:
            b[k] = a[i]
            b[k-1] = b[k]
            i, j, k = i-1, j-1, k-2

    while i >= 0:
        b[k] = a[i]
        i, k = i-1, k-1

    while j >= 0:
        b[k] = b[j]
        j, k = j-1, k-1

    return b


if __name__ == "__main__":
    n = 2
    arr1 = [11, 11]
    arr2 = [3, 11, 0, 0]
    print(merger_first_into_second(arr1, arr2))
