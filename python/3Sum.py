"""
Given an array of ints and a target sum K, find three numbers from the array
that add up to K (or return some Canary, if it doesn't exists)
"""

def sum2(arr, target):
    i = 0
    j = len(arr)-1
    while i<=j:
        add = arr[i] + arr[j]
        if add == target:
            return [arr[i], arr[j]]
        elif add > target:
            j -= 1 
        else:
            i += 1

    return None

def sum3(arr, target):
    arr.sort()  # inplace sort
    result = []
    i = 0
    while i < len(arr)-2:
        sum2result = sum2(arr[i+1:], target-arr[i])
        if sum2result is not None:
            result.append(arr[i])
            result.extend(sum2result)
            return result
        i += 1

    return None

if __name__ == "__main__":
    # arr = [5, 1, 4, 2, 7, 9, 0, 2, 4]
    arr = [-1, 0, 1, 2, -1, -4]
    target = 0

    print sum3(arr, target)
