class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ans = 0
        for sent in sentences:
            ans = max(ans, len(sent.split()))
        return ans
