from sys import stdin

def func_name(s):
    a = s.split('+')
    a.sort()
    return '+'.join(a)


if __name__ == '__main__':
    a = stdin.readline().strip()
    print(func_name(a))
