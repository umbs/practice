class Solution(object):
    def sortSentence(self, s: str) -> str:
        words = s.split()
        res = [None] * len(words)
        for word in words:
            idx = int(word[-1])-1
            res[idx] = word[:-1]
        return ' '.join(res)

if __name__ == "__main__":
    s = Solution()
    print(s.sortSentence("is2 sentence4 This1 a3"))
    print(s.sortSentence("Myself2 Me1 I4 and3"))
    # print(s.sortSentence())
