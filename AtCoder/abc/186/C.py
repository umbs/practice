N = input()

ans = 0

for i in range(int(N)):
    if '7' in str(i) or '7' in oct(i):
        continue
    ans += 1

print(ans)
