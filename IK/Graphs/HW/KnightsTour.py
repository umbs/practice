#!/bin/python

import sys

WHITE = 0
GRAY = 1
BLACK = 2
MIN_STEPS = 0


def within_bounds(rows, cols, x, y):
    return x >= 0 and x < rows and y >= 0 and y < cols


def moves(rows, cols, sr, sc, er, ec, path, visited):
    global MIN_STEPS
    if sr == er and sc == ec:
        MIN_STEPS = min(MIN_STEPS, len(path))
        print path
        return

    r = [-2, -2, -1, 1, -1, 1, 2, 2]
    c = [-1, 1, -2, -2, 2, 2, -1, 1]

    path.append((sr, sc))
    visited[sr][sc] = GRAY

    for i in range(0, 8):
        x = sr + r[i]
        y = sc + c[i]

        if not within_bounds(rows, cols, x, y):
            continue

        if visited[x][y] == WHITE:
            moves(rows, cols, x, y, er, ec, path, visited)

    path.pop()
    visited[sr][sc] = WHITE


def find_minimum_number_of_moves(rows, cols, sr, sc, er, ec):
    global MIN_STEPS
    visited = [[WHITE] * rows] * cols
    MIN_STEPS = rows * cols
    path = []
    moves(rows, cols, sr, sc, er, ec, path, visited)
    return MIN_STEPS


if __name__ == "__main__":
    f = sys.stdout

    '''
    rows = int(input())
    cols = int(input())
    start_row = int(input())
    start_col = int(input())
    end_row = int(input())
    end_col = int(input())
    '''
    rows = 5
    cols = 5
    start_row = 0
    start_col = 0
    end_row = 4
    end_col = 1

    res = find_minimum_number_of_moves(rows, cols, start_row,
                                start_col, end_row, end_col)

    f.write(str(res) + "\n")
    f.close()
