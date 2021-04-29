N, m, t = map(int, input().split())

n, last = N, 0
for _ in range(m):
  a, b = map(int, input().split())
  n -= a - last
  if n <= 0:
      print("No")
      exit()

  n = min(N, n+b-a)
  last = b

n -= t - last
if n <= 0:
    print("No")
else:
    print("Yes")
