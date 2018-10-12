import random


def solve(arr):
    e = 0
    o = len(arr)-1

    while True:
        while e <= o and arr[e]%2 == 0: e += 1
        while e <= o and arr[o]%2 == 1: o -= 1

        if e > o: break

        arr[e], arr[o] = arr[o], arr[e]


if __name__ == "__main__":
    arr = [random.randint(0, 25) for _ in range(10)]
    solve(arr)

    print(arr)
