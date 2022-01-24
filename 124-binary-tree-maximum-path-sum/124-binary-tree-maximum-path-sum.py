# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxSum = -math.inf
        self.dfs(root)
        return self.maxSum
    
    def dfs(self, node):
        if not node: return 0
        
        maxLeft = self.dfs(node.left)
        maxRight = self.dfs(node.right)
        
        maxLeft = max(maxLeft, 0)
        maxRight = max(maxRight, 0)
        
        localMax = maxLeft + maxRight + node.val
        self.maxSum = max(self.maxSum, localMax)
        
        return max(maxLeft, maxRight) + node.val
    