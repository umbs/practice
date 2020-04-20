class Solution(object):

    def __init__(self):
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'
        self.minTrans = 0

    def helper(self, beginWord, endWord, idx, exchNow, wordList):
        if idx == len(beginWord):
            if beginWord == endWord:
                self.minTrans = min(exchNow, self.minTrans)
                return

        for c in self.alphabet:
            tmp = beginWord[idx]
            beginWord[idx] = c
            if tmp != c and beginWord in wordList:
                exchNow += 1
                self.helper(beginWord, endWord, idx+1, exchNow, wordList)
                exchNow -= 1

            beginWord[idx] = tmp

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        self.maxLen = len(beginWord)
        self.helper(beginWord, endWord, 0, 0, wordList)

        return self.minTrans


if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
