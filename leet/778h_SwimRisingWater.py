import heapq


class Solution(object):
    def add_to_heap(self, x, y, LEN, visited):
        if (x, y) not in visited:
            return x >= 0 and x <= LEN-1 and y >= 0 and y <= LEN-1
        return False

    def swimInWater(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int

        - Maintain a min heap of (height, coordinates), sorted on height.
        - Pop the top element of the heap
        - When a cell is visited (filled with water), all it's adjacent,
          un-visited cells are added to the heap.
        - Loop through the heap until bottom right cell is top of the heap
        """

        visited = list()
        fill = list()
        X = [1, -1, 0, 0]
        Y = [0, 0, 1, -1]
        tyme = 0

        heapq.heappush(fill, (grid[0][0], 0, 0))
        visited.append((0, 0))

        while True:
            ht, x, y = heapq.heappop(fill)
            tyme = max(ht, tyme)

            if x == y == len(grid)-1:
                return tyme

            for i in range(4):
                a, b = x+X[i], y+Y[i]
                if self.add_to_heap(a, b, len(grid), visited):
                    heapq.heappush(fill, (grid[a][b], a, b))
                    visited.append((a, b))


s = Solution()
# print s.swimInWater([[0, 2], [1, 3]])
print s.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]])
