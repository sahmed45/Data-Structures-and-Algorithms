# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        currentNode = head
        position = 1
        startNew = head

        while position < left:
            startNew = currentNode
            currentNode = currentNode.next
            position += 1
        
        newList = None
        tail = currentNode
        while position >= left and position <= right:
            tempNext = currentNode.next
            currentNode.next = newList
            newList = currentNode
            currentNode = tempNext
            position += 1
        
        startNew.next = newList
        tail.next = currentNode
        
        if left > 1: return head
        else: return newList
        