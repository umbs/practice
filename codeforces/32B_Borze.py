from sys import stdin


def borze(code):
    res, i = '', 0
    while i < len(code):
        if code[i] is '.':
            res += '0'
            i += 1
        elif code[i] is '-':
            if i+1 == len(code):
                # Invalid code
                return res
            if code[i+1] is '.':
                res += '1'
            else:
                res += '2'
            i += 2
    return res


if __name__ == "__main__":
    code = stdin.readline().rstrip()
    print borze(code)
