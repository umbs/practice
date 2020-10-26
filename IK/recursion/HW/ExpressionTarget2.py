def generate_all_expressions(s, target):
    result = list()
    expr_so_far = s[0]
    helper(s, 1, target, expr_so_far, result)
    return result


def helper(s, start, target, expr_so_far, result):
    if start == len(s):
        if eval(expr_so_far) == target:
            result.append(expr_so_far)
        return

    helper(s, start+1, target, expr_so_far + str(s[start]), result)
    helper(s, start+1, target, expr_so_far + '+' + str(s[start]), result)
    helper(s, start+1, target, expr_so_far + '*' + str(s[start]), result)


if __name__ == "__main__":
    print(generate_all_expressions('050505', 5))
