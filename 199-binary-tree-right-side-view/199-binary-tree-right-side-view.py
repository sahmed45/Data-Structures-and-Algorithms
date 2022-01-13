# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return res
        
#         def dfs(node,level):

            
#             if level >= len(res):
#                 res.append(node.val)
            
#             if node.right:
#                 dfs(node.right,level + 1)
            
#             if node.left:
#                 dfs(node.left, level + 1)
                
#         dfs(root, 0)
#         return res

        q = deque()
        q.append(root)
        
        while q:
            level = len(q)
            
            for i in range(level):
                node = q.popleft()
                #if its the right most
                if i == level - 1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res
    