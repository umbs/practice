n, m, a, b = map(int, input().strip('\n').split())
cost = min(n*a, (n//m+1)*b, n//m*b + n%m*a)
print(cost)
