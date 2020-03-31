N = int(raw_input())
found = False
for i in range(1, 10):
    d, r = N/i, N%i
    if r == 0 and d < 10:
        found = True
        break

if found:
    print("Yes")
else:
    print("No")
