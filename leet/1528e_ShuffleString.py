class Solution(object):
    def restoreString(self, s, indices):
       r = ['-'] * len(s)
       for i in range(len(s)):
           r[indices[i]] = s[i]

       return ''.join(r)

if __name__ == "__main__":
    s = Solution()
    print(s.restoreString("codeleet", [4,5,6,7,0,2,1,3]))
