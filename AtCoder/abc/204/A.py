x, y = map(int, input().split())
z = (x+y)%3
if z:
    print(3-z)
else:
    print(z)
