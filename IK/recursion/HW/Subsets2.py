def generate_all_subsets(s):
    def helper(s, start, str_so_far, result):
        if start == len(s):
            result.append(str_so_far)
            return

        helper(s, start+1, str_so_far+s[start], result)
        helper(s, start+1, str_so_far, result)

    result = list()
    helper(s, 0, '', result)

    return result

if __name__ == "__main__":
    print(generate_all_subsets("xyz"))
