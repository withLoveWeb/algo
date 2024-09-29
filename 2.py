from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        l_ans=[]
        rank = 0
        
        if len(l1) >= len(l2):
            for n in range(len(l1)):
                try:
                    tmp = l1[n] + l2[n]
                except:
                    tmp = l1[n]
                if rank == 1:
                    tmp += 1
                    rank = 0
                if tmp >= 10:
                    tmp -= 10
                    rank = 1
                l_ans.append(tmp)
                
                if n == len(l1)-1 and rank == 1:
                    l_ans.append(1)
            return l_ans
        else:
            for n in range(len(l2)):
                try:
                    tmp = l1[n] + l2[n]
                except:
                    tmp = l2[n]
                if rank == 1:
                    tmp += 1
                    rank = 0
                if tmp >= 10:
                    tmp -= 10
                    rank = 1
                l_ans.append(tmp)
                
                if n == len(l2)-1 and rank == 1:
                    l_ans.append(1)
                        
            return l_ans
        
        
s = Solution()
print(s.addTwoNumbers([9], [9,9,9]))