class Solution(object):
    def checkIfPangram(self, sentence: str) -> bool:
        return len(set(sentence)) == 26

if __name__ == "__main__":
    s = Solution()
    print(s.checkIfPangram('thequickbrownfoxjumpsoverthelazydog'))
    print(s.checkIfPangram('leetcode'))
