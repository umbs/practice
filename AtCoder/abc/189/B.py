n, x = map(int, input().strip().split())
sum = 0

for i in range(n):
    v, p = map(int, input().split())
    sum += v*p
    if sum > x*100:
        print(i+1)
        break

if sum <= x*100:
    print(-1)
