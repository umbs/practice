"""
Pramp: 2/25/20. Question I have to ask. Time Planner

"""
def meeting_planner(slotsA, slotsB, dur):
  i, j = 0, 0

  while i < len(slotsA) and j < len(slotsB):
    a, b = slotsA[i]
    x, y = slotsB[j]

    # no overlap of intervals. Increment appropriate index
    if b < x:
      i += 1
      continue
    if y < a:
      j += 1
      continue

    # There is an interval overlap
    m = max(a, x)
    n = min(b, y)

    # Found an availability
    if m + dur <= n:
      return [m, m+dur]

    # No availability found. Figure out which index to increment.
    # slotsA interval is smaller. Increment it.
    if b < y:
      i += 1
    # slotsB interval is smaller. Increment it.
    else:
      j += 1

  return []
