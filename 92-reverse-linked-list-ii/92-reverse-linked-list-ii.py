# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        #dummy node to point at head
        #pointer to reach left
        
        dummy = ListNode(0, head)
        
        leftPrev, curr = dummy, head
        #to reach start of reversal
        for i in range(left - 1):
            leftPrev,curr= curr,curr.next
        
        #right - left + 1 reversals needed
        #curr is at left, prev is at before left
        prev = None
        for i in range(right - left + 1):
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        #link end of reversal
        leftPrev.next.next = curr
        #link start of reversal
        leftPrev.next = prev
        
        return dummy.next