N = int(input())

res = 0

for i in range(N+1):
    if i%3 and i%5:
        res += i

print(res)
