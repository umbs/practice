A, B = map(int, input().split())

def sum(n):
    ans = 0
    while n:
        ans += n%10
        n = n//10
    return ans

print(max(sum(A), sum(B)))
