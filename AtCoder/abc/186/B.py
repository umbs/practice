    h, w = map(int, input().split())
     
    lo, agg = 101, 0
     
    for i in range(h):
      a = list(map(int, input().split()))
      agg += sum(a)
      lo = min(lo, min(a))
     
    print(agg - (h*w*lo))
