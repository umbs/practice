class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = result = ListNode()
        head = head.next

        while head:
            result.val += head.val

            # End of list
            if self.terminal_node(head):
                return ans

            if head.val == 0:
                result.next = ListNode()
                result = result.next

            head = head.next

    def terminal_node(self, node) -> bool:
        return node.val == 0 and node.next is None
