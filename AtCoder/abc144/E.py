N, K = 11, 14
A = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
F = [8, 9, 7, 9, 3, 2, 3, 8, 4, 6, 2]

#N, K = map(int, raw_input().split())
#A = map(int, raw_input().split())
#F = map(int, raw_input().split())
A.sort(reverse=True)
F.sort(reverse=True)

print(A)
print(F)

for i in range(N):
    if K <= 0:
        break

    t = K
    K -= A[i]
    A[i] = max(A[i]-t, 0)

print(A)
print(F)
prod = [A[x] * F[N-x-1] for x in range(N)]
print(prod)
