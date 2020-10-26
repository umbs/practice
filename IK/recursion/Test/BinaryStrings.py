def bin_strings(s):
    def helper(L, idx, res):
        while idx < len(L) and L[idx] != '?':
            idx += 1

        if idx == len(L):
            res.add(''.join(L))
            return res

        L[idx] = '0'
        helper(L, idx+1, res)
        L[idx] = '1'
        helper(L, idx+1, res)
        # L[idx] = '?'

        return res

    res = set()
    return helper(list(s), 0, res)


if __name__ == "__main__":
    res = bin_strings('1?0?')
    print(list(res))

"""
             1?0?
            /     \
         100?     110?
      /    \      /    \
    1000   1001  1100  1101 
      ^     ^     x     ^
"""
