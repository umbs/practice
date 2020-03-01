def numberOfPaths(a):
    rows = len(a)
    cols = len(a[0])
    paths = [[0] * cols for i in range(rows)]

    for i in range(rows):
        if a[i][0] != 0:
            paths[i][0] = 1

    for i in range(cols):
        if a[0][i] != 0:
            paths[0][i] = 1

    for i in range(1, rows):
        for j in range(1, cols):
            paths[i][j] = paths[i-1][j] + paths[i][j-1]

    return paths[rows-1][cols-1]

if __name__ == "__main__":
    # a = [[1, 1]]
    # a = [[1, 1], [1, 1]]
    a = [   [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1],
        ]
    print(numberOfPaths(a))
