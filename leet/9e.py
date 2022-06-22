class Solution:
    def isPalindrome(self, x: int) -> bool:
        from collections import deque
        q = deque()
        
		# Negative numbers are *always NOT* a palindrome
        if x < 0:
            return False
        
        while x:
            q.append(x%10)
            x = x//10
        
        if len(q) == 1:
            return True
        
        while q:
            x, y = q.pop(), q.popleft()
            if x != y:
                return False
            
            if len(q) == 1:
                return True
        
        return True
