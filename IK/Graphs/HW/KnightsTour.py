from collections import deque

import sys

def is_valid(rows, cols, x, y):
    return 0 <= x and x < rows and 0 <= y and y < cols

def find_minimum_number_of_moves(rows, cols, sr, sc, er, ec):
    r = [-2, -2, -1, 1, -1, 1, 2, 2]
    c = [-1, 1, -2, -2, 2, 2, -1, 1]

    q = deque([(sr, sc, 0)])
    visited = set((sr, sc))

    while q:
        row, col, count = q.popleft()

        if (row, col) == (er, ec):
            return count

        for i in range(8):
            x, y = row + r[i], col + c[i]
            if not is_valid(rows, cols, x, y):
                continue

            if (x, y) not in visited:
                visited.add((x, y))
                q.append((x, y, count+1))

    return -1


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
    start_row = 1
    start_col = 1
    end_row = 4
    end_col = 4

    res = find_minimum_number_of_moves(rows, cols, start_row,
                                start_col, end_row, end_col)

    f.write(str(res) + "\n")
    f.close()
