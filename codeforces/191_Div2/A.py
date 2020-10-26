n = int(input())
nums = list(map(int, input()))

i, j, res = 0, 0, 0
while j < n and nums[j] == 0:
    j += 1

while j < n and nums[j] == 1:
    j += 1

