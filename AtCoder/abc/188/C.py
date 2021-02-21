n = int(input())
a = list(map(int, input().split()))

mid = 2 ** (n-1)

left = max(a[:mid])
right = max(a[mid:])
large = min(left, right)
print(1+a.index(large))
