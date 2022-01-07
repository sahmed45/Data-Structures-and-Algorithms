"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        currentNode = head

        while currentNode:
            if not currentNode.child:
                currentNode = currentNode.next
            else:
                tail = currentNode.child
                while tail.next:
                    tail = tail.next
                tail.next = currentNode.next
                if tail.next:
                    tail.next.prev = tail
                currentNode.next = currentNode.child
                currentNode.next.prev = currentNode
                currentNode.child = None
        return head
            