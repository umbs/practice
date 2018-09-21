from sys import stdin


def is_distinct(N):
    dig = []
    for i in range(4):
        r = N % 10
        if r in dig:
            return False
        else:
            dig.append(r)
        N = N/10

    return True


def func_name(N):
    N += 1
    while not is_distinct(N):
        N += 1
    return N


if __name__ == '__main__':
    '''
    - Use following methods
        * stdin.readlines() to read all lines
        * stdin.readline() to read a line
        * stdin.read()
        * rstrip()
        * split()
    '''
    N = int(stdin.readline().rstrip())
    print func_name(N)
