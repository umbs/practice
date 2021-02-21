""" Saw solution in editorial
https://atcoder.jp/contests/abc188/editorial/556
"""
N, C = map(int, input().split())
event = []

for i in range(N):
  a, b, c = map(int, input().split())
  a -= 1
  event.append((a, c))
  event.append((b, -c))
  
ans, fee, idx = 0, 0, 0
event.sort()

for x, y in event:
  if x != idx:
    ans += min(C, fee) * (x-idx)
    idx = x
  fee += y

print(ans)
