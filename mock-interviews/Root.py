"""
Pramp: Mar 1, 2020
"""
def root(x, n):
  """ Find n'th root of x, within 0.001 error. Binary search between 0 to x, using pow() function """
  y = float(x)
  delta = pow(y, n) - x
  lo, hi = 0.0, float(x)
  mid = (hi + lo)/2

  while abs(delta) >= 0.001:
    if delta > 0:
      y = (mid + lo)/2
      hi = mid
    elif delta < 0:
      y = (mid + hi)/2
      lo = mid

    mid = (hi + lo)/2
    delta = pow(y, n) - x

  return y

print(root(7, 3))
print(root(10000, 9))
