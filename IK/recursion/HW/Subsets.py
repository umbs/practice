def subsets(s, start, substr, res):
    if start >= len(s):
        res.append(substr)
        return

    # with the char at start index
    subsets(s, start+1, substr+s[start], res)
    # without the char at start index
    subsets(s, start+1, substr, res)

def generate_all_subsets(s):
    res = []
    substr = ''
    subsets(s, 0, substr, res)
    return res

if __name__ == "__main__":
    s = "xyz"
    print(generate_all_subsets(s))
