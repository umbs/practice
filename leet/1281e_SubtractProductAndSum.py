class Solution(object):
    def subtractProductAndSum(self, n):
        p, s, N = 1, 0, n
        
        while N:
            p *= N%10
            s += N%10
            N = N/10
        
        return p-s
