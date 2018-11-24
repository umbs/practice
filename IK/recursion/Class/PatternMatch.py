def helper(src, src_idx, pat, pat_idx):
    if src_idx == len(src) and pat_idx == len(pat):
        return True

    if src_idx == len(src) or pat_idx == len(pat):
        return False

    if src[src_idx] == pat[pat_idx] or pat[pat_idx] == '.':
        return helper(src, src_idx+1, pat, pat_idx+1)

    if pat[pat_idx] == '*':
        return helper(src, src_idx, pat, pat_idx+1) or helper(src, src_idx+1, pat, pat_idx)

    return False

def pattern_match(src, pat):
    '''
    * indicates zero or more chars
    . indicates just one char (any char)
    pattern must match in full
    '''
    return helper(src, 0, pat, 0)


if __name__ == "__main__":
    # print(pattern_match("Hello", "H*.lo"))
    print(pattern_match("ababcba", "ab*b*"))
