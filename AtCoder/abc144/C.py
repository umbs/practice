import math

N = int(raw_input())
mov = N-1

for i in range(2, int(math.sqrt(N))+1):
    if N%i == 0:
        mov = min(mov, (i-1) + (N/i-1))

print(mov)
