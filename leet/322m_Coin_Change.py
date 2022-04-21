from typing import List
from collections import deque

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        que = deque([(0, 0)])
        visited = [True] + [False] * amount

        while que:
            count, value = que.popleft()
            count += 1

            for coin in coins:
                new_value = value + coin
                if new_value == amount:
                    return count

                if new_value < amount:
                    if visited[new_value ] is False:
                        visited[new_value] = True
                        que.append((count, new_value))

        return -1

if __name__ == "__main__":
    s = Solution()
    ans = s.coinChange([1], 2)
    print(ans)
