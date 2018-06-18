class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        list = []
        
        for word in words:
            mc = ""
            for c in word:
                mc = mc + morse[ord(c)-ord('a')]
            print(mc)

s = Solution()
s.uniqueMorseRepresentations("abc")
