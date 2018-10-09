from sys import stdin

def func_name():
    pass


if __name__ == '__main__':
    '''
    - Use following methods
        * stdin.readlines() to read all lines
        * stdin.readline() to read a line
        * stdin.read()
        * rstrip()
        * split()
    func_name()
    '''
    r1 = stdin.readline().rstrip().split()
    r2 = stdin.readline().rstrip().split()
    r3 = stdin.readline().rstrip().split()

    r1 = map(int, r1)
    r2 = map(int, r2)
    r3 = map(int, r3)

    print r1, r2, r3
