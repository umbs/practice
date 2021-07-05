class Solution(object):
    def truncateSentence2(self, s: str, k: int) -> str:
        res = s.split()[:k]
        return ' '.join(res)

    def truncateSentence(self, s: str, k: int) -> str:
        for i in range(len(s)):
            if s[i] == ' ':
                k -= 1
                if k == 0:
                    return s[:i]

        return s


if __name__ == "__main__":
    s = Solution()
    print(s.truncateSentence("Hello how are you Contestant", k = 4))
    print(s.truncateSentence("What is the solution to this problem", k = 4))
    print(s.truncateSentence("chopper is not a tanuki", k = 5))
