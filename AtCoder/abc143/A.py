A, B = map(int, raw_input().split())
res = A - 2*B
if res <= 0:
	res = 0
print(res)
