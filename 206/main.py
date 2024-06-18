# Reverse Linked List
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# 1 -> 2 -> 3 -> 4
# 4 -> 3 -> 2 -> 1
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        def reverse(list : Optional[ListNode], next = None):
            if not list.next:
                return ListNode(list.val, next)
            return reverse(list.next, ListNode(list.val, next))
        return reverse(head)


s = Solution()
list = ListNode(1, ListNode(2, ListNode(3)))
print(s.reverseList(list))