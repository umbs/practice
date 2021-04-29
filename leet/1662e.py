class Solution(object):
    def arrayStringsAreEqual(self, w1, w2):
        return "".join(w1) == "".join(w2)

if __name__ == "__main__":
    s = Solution()
    print(s.arrayStringsAreEqual(["ab", "c"], ["a", "bc"]))
    print(s.arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))
    print(s.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"]))
