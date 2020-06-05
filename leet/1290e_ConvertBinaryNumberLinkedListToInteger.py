class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        res = head.val
        while head.next:
            head = head.next
            res = (2 * res) + head.val
        return res
