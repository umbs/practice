def generate_all_expressions(s, target):
    exp_so_far = s[0]
    result = list()
    helper(s, 1, target, exp_so_far, result)
    return result


def helper(s, start, target, exp_so_far, result):
    if start == len(s):
        if eval_expr(exp_so_far) == target:
            result.append(exp_so_far)
        return

    helper(s, start+1, target, exp_so_far+'+'+s[start], result)
    helper(s, start+1, target, exp_so_far+'*'+s[start], result)
    helper(s, start+1, target, exp_so_far+s[start], result)


def eval_expr(expr):
    toks = expr.split('+')

    value = 0
    for t in toks:
        if not t:
            continue

        product = 1

        if '*' in t:
            nums = t.split('*')
            for p in nums:
                product *= int(p)
            value += product
        else:
            value += int(t)

    print(expr, value)
    return value



if __name__ == "__main__":
    # print(generate_all_expressions("2022", 24))
    print(generate_all_expressions("050505", 5))
    # print(generate_all_expressions("40404040", 0))
