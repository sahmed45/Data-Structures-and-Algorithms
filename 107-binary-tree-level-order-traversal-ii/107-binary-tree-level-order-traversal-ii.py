# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        #using normal list
#         if not root: return []
#         q = deque([root])
#         res = []
#         while q:
#             level = []
#             for _ in range(len(q)):
#                 node = q.popleft()
#                 level.append(node.val)
                
#                 if node.left:
#                     q.append(node.left)
#                 if node.right:
#                     q.append(node.right)
#             res.append(level)
            
#         return res[::-1]


#          using queue for result and appending left for reverse order

        if not root: return []
        q = deque([root])
        res = deque()
        
        while q:
            level = []
            for _ in range(len(q)):
                node = q.popleft()
                level.append(node.val)
                
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            res.appendleft(level)
        return res