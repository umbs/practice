def subsets(s, start, substr, res):
    if start >= len(s):
        res.append(substr)
        return

    # without the char at start index
    subsets(s, start+1, substr, res)
    # with the char at start index
    subsets(s, start+1, substr+s[start], res)

def generate_all_subsets(s):
    res = []
    substr = ''
    subsets(s, 0, substr, res)
    return res

if __name__ == "__main__":
    s = "abc"
    print(generate_all_subsets(s))
