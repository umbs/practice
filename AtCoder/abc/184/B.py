N, X = map(int, input().split())
S = input()

for c in S:
    if c == 'x':
        X = max(0, X-1)
    else:
        X += 1

print(X)
