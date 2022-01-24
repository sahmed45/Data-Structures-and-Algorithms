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
    # ignore paths with negative sums, since we need to find the maximum sum we should
    # ignore any path which has an overall negative sum.
        maxLeft = max(maxLeft, 0)
        maxRight = max(maxRight, 0)
    # maximum path sum at the current node will be equal to the sum from the left subtree +
    # the sum from right subtree + val of current node   
        localMax = maxLeft + maxRight + node.val
     # update the global maximum sum
        self.maxSum = max(self.maxSum, localMax)
    # maximum sum of any path from the current node will be equal to the maximum of
    # the sums from left or right subtrees plus the value of the current node        
        return max(maxLeft, maxRight) + node.val
    