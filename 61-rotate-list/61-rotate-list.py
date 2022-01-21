# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # get the length, # of jumps is k - length - 1
        if not head: return None
        if not head.next: return head
        
        length, tail = 1, head
        
        while tail.next:
            tail = tail.next
            length += 1
        #incase k > length, the remainder equals rotations    
        k = k % length
        if k == 0:
            return head
        
        curr = head
        for i in range(length - k - 1):
            curr = curr.next
        
        #next head will be at rotate position.next
        newHead = curr.next
        #this position will be end
        curr.next = None
        tail.next = head
        
        return newHead