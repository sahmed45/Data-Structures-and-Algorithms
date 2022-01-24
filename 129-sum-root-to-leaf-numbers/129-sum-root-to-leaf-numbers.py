# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        ans = 0
        return self.dfs(root, ans)
        
    def dfs(self, node, currVal):
        if not node: return 0
        
    
        currVal = (currVal *(10)) + node.val
            
        if not node.left and not node.right:

            return currVal
        return self.dfs(node.left, currVal) + self.dfs(node.right, currVal)
        
