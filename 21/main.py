from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        def merge(list1,list2):
            if list1 == None:
                return list2
            elif list2 == None:
                return list1
            if list1.val < list2.val:
                list1.next = merge(list1.next, list2)
                return list1
            else:
                list2.next = merge(list1, list2.next)
                return list2
        
        return merge(list1,list2)


s = Solution()
list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
merged_list = s.mergeTwoLists(list1,list2)

while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next