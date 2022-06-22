# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        from collections import deque
        qu = deque()
        
        temp = head
        while temp:
            qu.append(temp.val)
            temp = temp.next

        idx = 0
        while qu:
            end = qu.pop()
            if head[idx].val != end:
                return False
            
            idx += 1
        
        return True
