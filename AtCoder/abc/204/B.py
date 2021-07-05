N = map(int, input())
A = map(int, input().split())

res = 0

for a in A:
    if a <= 10:
        continue
    res += a-10

print(res)
