# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []
        self.dfs(root, targetSum, [], res)
        return res
        
    def dfs(self, node, reqSum, currPath, res):
            if not node: return 
            currPath.append(node.val)
            reqSum -= node.val
            
            if reqSum == 0 and not node.left and not node.right:
                res.append(list(currPath))
            else:
                self.dfs(node.left,reqSum,currPath,res)
                self.dfs(node.right,reqSum, currPath, res)
            currPath.pop()
