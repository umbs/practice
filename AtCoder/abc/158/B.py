S = str(raw_input())
N = len(S)

rev = S[::-1]
S1 = S[:(N-1)/2]
S2 = S[(N+1)/2:]

if (rev == S and S1[::-1] == S[:(N-1)/2] and S2[::-1] == S[(N+1)/2:]):
    print("Yes")
else:
    print("No")
