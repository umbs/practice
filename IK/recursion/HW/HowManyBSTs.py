from random import randint
from time import time

mem = {0: 1, 1: 1}


def countTree(num):
    if num <= 1:
        return 1

    if num in mem:
        return mem[num]

    count = 0
    for i in range(1, num+1):
        left = countTree(i-1)
        right = countTree(num-i)
        count += left * right

    mem[num] = count

    return count


def how_many_BSTs(n):
    return countTree(n)


if __name__ == "__main__":
    start = time()
    for _ in range(1000000):
        how_many_BSTs(randint(1, 25))
    end = time()
    print(end-start)
