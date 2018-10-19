ops = ['+', '*']


def generate_all_expressions(s, target):
    exp_so_far = ""
    return gen_all_exp_utils(s, 0, exp_so_far, target)


def gen_all_exp_utils(s, start, exp_so_far, target):
    if start == len(s):
        # TODO
        return

    i = start

    while i < len(s):
        for i in range(2):
            exp_so_far += ops[i] + s[
