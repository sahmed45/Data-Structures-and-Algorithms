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
            #add current node
            currPath.append(node.val)
            reqSum -= node.val
            
            if reqSum == 0 and not node.left and not node.right:
                #have to use list() or [:] or a reference to original is made, this copies it
                res.append(currPath[:])
            else:
                self.dfs(node.left,reqSum,currPath,res)
                self.dfs(node.right,reqSum, currPath, res)
            #pop node when done processing
            currPath.pop()
