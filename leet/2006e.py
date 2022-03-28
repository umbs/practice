from typing import List
import pdb

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        hmap, count = dict(), 0
        for i, n in enumerate(nums):
            if k-n in hmap:
                count += len(hmap.get(k-n))
            elif n-k in hmap:
                count += len(hmap.get(n-k))
            
            value = hmap.get(n, list())
            hmap[n] = value.append(i)

        return count

if __name__ == "__main__":
    s = Solution()
    print(s.countKDifference([1,2,2,1], 1))
