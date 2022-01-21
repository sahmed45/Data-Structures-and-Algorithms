"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root: return root
        
        q = deque([root])
        
        while q:
            prevNode = None
            for _ in range(len(q)):
                node = q.popleft()
                # point previous to next
                if prevNode:
                    prevNode.next = node
                prevNode = node
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
        return root
                    