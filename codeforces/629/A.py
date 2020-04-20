N = int(input())

for i in range(N):
    a, b = map(int, input().split())
    if a % b == 0:
        print(0)
    else:
        div = 1 + a//b
        inc = (div * b) - a
        print(inc)
