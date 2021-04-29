class Solution(object):
    def countConsistentStrings(self, allowed, words):
        ok = set(allowed)
        cnt = 0
        for s in words:
            chars = set(s)
            if chars.issubset(ok):
                cnt += 1

        return cnt

if __name__ == "__main__":
    s = Solution()
    print(s.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"]))
    print(s.countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"]))
    print(s.countConsistentStrings("cad", ["cc","acd","b","ba","bac","bad","ac","d"]))
