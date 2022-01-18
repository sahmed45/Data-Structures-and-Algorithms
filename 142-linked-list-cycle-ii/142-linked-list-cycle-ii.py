# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
            
            if fast == slow:
                #the next time they meet is intersection
                slow = head
                while fast != slow:
                    slow = slow.next
                    fast = fast.next
                return slow
        return None