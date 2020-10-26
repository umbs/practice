B = int(input())
boys = list(map(int, input().strip('\n').split()))
boys.sort()
G = int(input())
girls = list(map(int, input().strip('\n').split()))
girls.sort()

i, j = 0, 0
pairs = 0

while i < len(boys) and j < len(girls):
    if abs(boys[i] - girls[j]) <= 1:
        pairs += 1
        i += 1
        j += 1
    elif boys[i] < girls[j]:
        i += 1
    else:
        j += 1

print(pairs)
