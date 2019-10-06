_, l = map(int, raw_input().split())
h = list(map(int, raw_input().split()))

cnt = 0
for i in h:
    if i >= l:
        cnt += 1

print cnt
