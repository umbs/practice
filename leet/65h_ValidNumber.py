"""
Link: https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
One of the comments have detailed explanation
"""

class Solution(object):
  def isNumber(self, s):
      """
      :type s: str
      :rtype: bool
      """
      #define a DFA
      state = [{}, 
              {'blank': 1, 'sign': 2, 'digit':3, '.':4}, 
              {'digit':3, '.':4},
              {'digit':3, '.':5, 'e':6, 'blank':9},
              {'digit':5},
              {'digit':5, 'e':6, 'blank':9},
              {'sign':7, 'digit':8},
              {'digit':8},
              {'digit':8, 'blank':9},
              {'blank':9}]
      currentState = 1
      for c in s:
          if c >= '0' and c <= '9':
              c = 'digit'
          if c == ' ':
              c = 'blank'
          if c in ['+', '-']:
              c = 'sign'
          if c not in state[currentState].keys():
              return False
          currentState = state[currentState][c]
      if currentState not in [3,5,8,9]:
          return False
      return True


"""
class Solution(object):

    def eps(self, s):
        if not s:
            return False

        if (s[0] < '0' or s[0] > '9') and s[0] not in '-+':
            return False

        for i in range(1, len(s)):
            if (s[i] < '0' or s[i] > '9'):
                return False

        return True

    def dot(self, s):
        if not s:
            return False

        if s[0] < '0' or s[0] > '9':
            return False

        for i in range(1, len(s)):
            if (s[i] < '0' or s[i] > '9') and s[i] != 'e':
                return False

            if s[i] == 'e':
                return self.eps(s[i+1:])
        
        return True


    def start(self, s):
        if not s:
            return False

        while '0' <= s[0] <= '9':
            return self.start(s[1:])

        if s[0] == '.':
            return self.dot(s[1:])

        if s[0] == 'e':
            return self.eps(s[1:])

        return False

    def isNumber(self, s):
        # :type s: str
        # :rtype: bool

        s = s.strip()

        if s[0] not in '-+0123456789':
            return False

        if s[0] == '-' or s[0] == '+':
            return self.start(s[1:])

        return self.start(s)
"""


if __name__ == "__main__":
    s = Solution()
    print("0 ==> " + str(s.isNumber("0")))
    print(" 0.1 ==> " + str(s.isNumber(" 0.1")))
    print("abc ==> " + str(s.isNumber("abc")))
    print("1 a ==> " + str(s.isNumber("1 a")))
    print("2e10 ==> " + str(s.isNumber("2e10")))
    print(" -90e3 ==> " + str(s.isNumber(" -90e3")))
    print(" 1e ==> " + str(s.isNumber(" 1e")))
    print(" e3 ==> " + str(s.isNumber(" e3")))
    print(" 6e-1 ==> " + str(s.isNumber(" 6e-1")))
    print(" 99e2.5 ==> " + str(s.isNumber(" 99e2.5")))
    print(" 53.5e93 ==> " + str(s.isNumber(" 53.5e93")))
    print(" --6 ==> " + str(s.isNumber(" --6")))
    print(" -+3 ==> " + str(s.isNumber(" -+3")))
    print("95a54e53 ==> " + str(s.isNumber("95a54e53")))
