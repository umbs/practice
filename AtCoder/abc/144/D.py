import math

a, b, x = map(float, raw_input().split())

if (a*a*b)/2 > x:
    y = float(2*x/(a*b)) 
    print(math.degrees(math.atan(b/y)))
else:
    i = 2*b - (2*x/a**2)
    print(math.degrees(math.tan(i/a)))
