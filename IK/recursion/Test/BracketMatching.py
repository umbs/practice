def util(n, opn, cls, substr, result):
    if opn < cls:
        return

    if opn > n:
        return

    if n == opn and opn == cls:  # a matching set of braces
        result.append(substr)
        return

    util(n, opn+1, cls, substr+"(", result)
    util(n, opn, cls+1, substr+")", result)


def find_all_well_formed_brackets(n):
    result = []
    substr = ''
    util(n, 0, 0, substr, result)
    return result


if __name__ == "__main__":
    print(find_all_well_formed_brackets(2))
