#
# Complete the dutch_flag_sort function below.
#


def dutch_flag_sort(balls):
    r, b = 0, len(balls)-1

    l = list(balls)

    i = 0
    while i <= b:
        if l[i] is 'R':
            l[r], l[i] = l[i], l[r]
            r, i = r+1, i+1
        elif l[i] is 'G':
            i += 1
        elif l[i] is 'B':
            l[b], l[i] = l[i], l[b]
            b = b-1

    return (''.join(str(e) for e in l))

if __name__ == "__main__":
    balls = "GBGGRBRGRRGGBBBRRRBBBBRB"
    print(dutch_flag_sort(balls))
