def is_palindrome(s, start, offset):
    i, j = start, start+offset-1

    while i < j:
        if s[i] != s[j]:
            return False
        i, j = i+1, j-1

    return True


def paly(s, L, res):
    if L == 0:
        return

    i = 0
    substr = ''
    while i+L <= len(s):
        if is_palindrome(s, i, L):
            substr += s[i:i+L] + "|"
        i += 1

    if substr:
        substr = substr[:len(substr)-1]  # remove trailing "|"
        res.append(substr)
    paly(s, L-1, res)


def palindrome(s):
    res = []
    paly(s, len(s), res)
    print(res)


if __name__ == "__main__":
    s = "abracadabra"
    palindrome(s)
