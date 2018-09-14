"""
http://codeforces.com/problemset/problem/69/A
"""


def space():
    count = int(raw_input())
    vec = list()
    result = [0, 0, 0]

    for _ in range(count):
        force = raw_input().split(' ')
        # print type(force)
        vec.append(force)
        result[0] += int(force[0])
        result[1] += int(force[1])
        result[2] += int(force[2])

    if result[0] == 0 and result[1] == 0 and result[2] == 0:
        return "YES"

    return "NO"


if __name__ == "__main__":
    print space()
