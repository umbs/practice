class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        cnt = set()

        for word in words:
            mc = [] 
            for c in word:
                mc.append(morse[ord(c)-ord('a')])
            cnt.add(''.join(mc))
        return len(cnt)

s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))
