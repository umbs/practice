class Solution(object):
    def decode(self, en, fi):
        res = [fi]
        for i in range(len(en)):
            res.append(en[i]^res[i])

        return res

if __name__ == "__main__":
    s = Solution()
    print(s.decode([1,2,3], 1))
    print(s.decode([6,2,7,3], 4))
