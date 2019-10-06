from sys import stdin


def change(S, K):
    c = 0

    if len(S) == 1:
        return K/2

    i = 1
    while i < len(S):
        if S[i-1] == S[i]:
            c += 1
            i += 2
        else:
            i += 1

    if i == len(S) and S[-1] == S[0] and S[-1] != S[-2]:
        c += 1

    return K * c


if __name__ == "__main__":
    S = stdin.readline().strip()
    K = int(stdin.readline())

    print(change(S, K))
