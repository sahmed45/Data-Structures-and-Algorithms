# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        currentLevel = 0
        
        def dfs(node,currentLevel, res):
            if not node: return res
            
            if currentLevel >= len(res):
                res.append(node.val)
            
            if node.right:
                dfs(node.right,currentLevel + 1,res)
            
            if node.left:
                dfs(node.left, currentLevel + 1, res)
                
        dfs(root, currentLevel, res)
        return res