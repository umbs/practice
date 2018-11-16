def countWaysToClimb(steps, n):
    res = [0] * (n+1)

    for i in range(0, n+1):
        for s in steps:
            if i == s:
                res[i] += 1

            elif i > s:
                res[i] += res[i-s]

    return res[n]


if __name__ == "__main__":
    steps = [2, 3]
    n = 7
    res = countWaysToClimb(steps, n)
    print(res)
