import sys


def move_letters_to_left_side_with_minimizing_memory_writes(s):
    arr = list(s)

    wrt, ex = -1, -1

    # find first writable position
    for i in range(0, len(arr)):
        if arr[i].isdigit():
            wrt = i
            break

    # String has no digit
    if wrt == -1:
        return s

    ex = wrt + 1

    while ex < len(arr):
        if arr[ex].isdigit():
            ex += 1
        else:
            arr[wrt] = arr[ex]
            wrt, ex = wrt + 1, ex + 1

    return ''.join(arr)


if __name__ == "__main__":
    fptr = sys.stdout

    # s = input()
    s = 'kkkkKkkkkk'

    res = move_letters_to_left_side_with_minimizing_memory_writes(s)

    fptr.write(res + '\n')

    fptr.close()
