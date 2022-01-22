# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         #O n
#         if not root: return 0
        
#         count = 0
#         q = deque([root])
        
#         while q:
#             for _ in range(len(q)):
#                 count += 1
#                 node = q.popleft()
                
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#         return count