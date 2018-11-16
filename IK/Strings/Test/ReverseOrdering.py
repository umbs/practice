import sys


def reverse_ordering_of_words(s):
    arr = list(s)
    res = list()
    i = len(arr)-1
    j = 0

    while i >= 0:
        if arr[i] == ' ':
            res.append(arr[i])
            i -= 1
        else:
            j = i-1
            while j >= 0 and arr[j] != ' ':
                j -= 1

            res.extend(arr[j+1:i+1])
            i = j

    print(res)
    return ''.join(res)


if __name__ == "__main__":
    fptr = sys.stdout

    # s = input()
    s = "I       will do it."

    res = reverse_ordering_of_words(s)

    fptr.write(res + '\n')

    fptr.close()
