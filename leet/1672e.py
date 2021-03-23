class Solution(object):
    def maximumWealth(self, acc):
        rich = 0
        for i in range(len(acc)):
            rich = max(rich, sum(acc[i]))

        return rich


if __name__ == "__main__":
    s = Solution()
    print(s.maximumWealth([[1,2,3],[3,2,1]]))
    print(s.maximumWealth([[1,5],[7,3],[3,5]]))
    print(s.maximumWealth([[2,8,7],[7,1,3],[1,9,5]]))
