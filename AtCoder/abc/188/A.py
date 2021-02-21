x, y = map(int, input().split())
if x < y and y-x < 3:
    print("Yes")
elif y < x and x-y < 3:
    print("Yes")
else:
    print("No")
