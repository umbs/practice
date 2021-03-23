class Solution(object):
    def interpret(self, cmd):
        res = []
        i = 0
        while i < len(cmd):
            if cmd[i] == 'G':
                res.append('G')
                i += 1
            elif cmd[i:i+2] == '()':
                res.append('o')
                i += 2
            elif cmd[i:i+4] == '(al)':
                res.append('al')
                i += 4
            else:
                i += 1

        return "".join(res)

if __name__ == "__main__":
    s = Solution()
    print(s.interpret("G()(al)"))
    print(s.interpret("G()()()()(al)"))
    print(s.interpret("(al)G(al)()()G"))
