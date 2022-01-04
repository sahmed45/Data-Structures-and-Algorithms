# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        position = 1
        currentNode = head
        startPrev = head
        tempNext = head
        prev = None
        while position < left:
            startPrev = currentNode
            currentNode = currentNode.next
            position += 1
        
        tail = currentNode
        
        while position >= left and position <= right:
            tempNext = currentNode.next
            currentNode.next = prev
            prev = currentNode
            currentNode = tempNext
            position += 1
        
        startPrev.next = prev
        
        tail.next = currentNode
        
        if left > 1: return head
        else: return prev
        
        