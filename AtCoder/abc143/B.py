N = int(raw_input())
num = list(map(int, raw_input().split()))

res = 0

for i in range(N):
    for j in range(i, N):
        if i == j:
            continue
        res += num[i] * num[j]

print(res)
