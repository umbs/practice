N = int(input())
points = []

for i in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

points.sort()

cnt = 0

for i in range(N):
    for j in range(i+1, N):
        x1, y1 = points[i]
        x2, y2 = points[j]
        slope = float((y2-y1)/(x2-x1))

        if slope <= 1 and slope >= -1:
            cnt += 1

print(cnt)
