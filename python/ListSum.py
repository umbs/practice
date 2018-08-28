"""
Problem Description: Add two numbers, represented as linked lists (lists)

Example:
    451+724 = 1175
    [4, 5, 1] + [7, 2, 4] = [1, 1, 7, 5]

Solution/Algorithm:

Pseudocode:

"""

def list_sum(a, b):
    i = len(a)-1
    j = len(b)-1
    carry = 0
    result = []

    while i >= 0 or j>=0:
        add = 0
        if i>=0:
            add += a[i]
        if j>=0:
            add += b[j]

        add += carry

        if add >= 10:
            carry = 1
            add %= 10
        result.insert(0, add)
        i -= 1
        j -= 1

    if carry == 1:
        result.insert(0, carry)

    return result


if __name__ == "__main__":
    a = [4, 5, 1]
    b = [7, 2, 4]

    print list_sum(a, b)
