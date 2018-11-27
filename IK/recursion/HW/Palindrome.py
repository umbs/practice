def is_palindrome(s, l, r):
    while l < r:
        if s[l] != s[r]:
            return False
        l, r = l+1, r-1
    return True


def palindrome(s):
    result = list()
    for width in range(0, len(s)):
        found = ''
        for i in range(0, len(s)-width):
            if is_palindrome(s, i, i+width):
                found += s[i:i+width+1] + '|'

        result.append(found)

    return result


if __name__ == "__main__":
    s = "abracadabra"
    # s = "aba"
    print(palindrome(s))
