def brackets(n):
    def helper(n, o, c, running, result):
        if c == n:
            result.append(running)
            return result

        if o < n:
            helper(n, o+1, c, running + '(', result)
        if c < o:
            helper(n, o, c+1, running + ')', result)

        return result

    result = list()
    return helper(n, 0, 0, '', result)

if __name__ == "__main__":
    n = 11 
    # print(brackets(n))
    print(len(brackets(n)))
