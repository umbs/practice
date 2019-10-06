N = int(raw_input())
O = list(map(int, raw_input().split()))

res = {}
for i in range(N):
    res[O[i]] = i

result = []
for i in range(N):
    result.append(res[i+1])

print(' '.join(str(x+1) for x in result))
