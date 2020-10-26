from sys import stdin

def move_boys(que, T):
    N = len(que)
    while T > 0:
        i = 1
        while i < N:
            if que[i-1] == 'B' and que[i] == 'G':
                que[i-1], que[i] = que[i], que[i-1]
                i += 1
            i += 1
        T -= 1

    print ''.join(que)


if __name__ == '__main__':
    N, T = stdin.readline().rstrip().split()
    que = list(stdin.readline().rstrip())
    move_boys(que, int(T))
