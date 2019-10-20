N = int(raw_input())
S = str(raw_input())

r = [S[0]]

for i in range(1, N):
    if S[i] != S[i-1]:
        r.append(S[i])

print(len(r))
