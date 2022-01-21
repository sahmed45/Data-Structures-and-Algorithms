# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = deque()
        q = deque([root])
        zigZag = False
        while q:
            level = []  
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                    
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                    
            if  zigZag:         
                res.append(level[::-1])
                zigZag = False
            else:
                res.append(level)
                zigZag = True
            
        return res