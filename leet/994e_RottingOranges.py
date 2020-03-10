from collections import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # Build rot que
        rot = deque()
        X = len(grid)
        Y = len(grid[0])
        fresh = 0

        for i in range(X):
            for j in range(Y):
                if grid[i][j] == 2:
                    rot.append((i,j))
                elif grid[i][j] == 1:
                    fresh += 1

        minute = 0
        # BFS starting with 'rot' que
        while rot:
            sz = len(rot)

            for i in range(sz):
                i, j = rot.popleft()

                if i-1 >= 0 and grid[i-1][j] == 1:
                    grid[i-1][j] = 2
                    rot.append((i-1, j))

                if i+1 < X and grid[i+1][j] == 1:
                    grid[i+1][j] = 2
                    rot.append((i+1, j))

                if j-1 >= 0 and grid[i][j-1] == 1:
                    grid[i][j-1] = 2
                    rot.append((i, j-1))

                if j+1 < Y and grid[i][j+1] == 1:
                    grid[i][j+1] = 2
                    rot.append((i, j+1))

            fresh -= len(rot)

            if rot:
                minute += 1

        if fresh:
            return -1

        return minute


if __name__ == "__main__":
    s = Solution()
    # print s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
    print s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]])
