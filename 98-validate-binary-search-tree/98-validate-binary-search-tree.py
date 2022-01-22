# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        
        def valid(node, low = -math.inf, high=math.inf):
            if not node:
                return True
            if not (node.val < high and node.val > low):
                return False
            
            return (valid(node.left, low, node.val) and valid(node.right, node.val, high))
        
        return valid(root)