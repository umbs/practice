line = input()
n, l = map(int, line.split(' '))

line = input()
points = list(map(int, line.split(' ')))
points.sort()

d = max(points[0], l - points[-1])
for i in range(1, len(points)):
    d = max(d, (points[i] - points[i-1])/2)

print(d)
