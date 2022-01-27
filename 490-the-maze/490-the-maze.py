class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        # maze dimension
        height = len(maze)
        width = len(maze[0])
        
		# record where the ball stopped and continue choosing new directions
        marker = [[False for _ in range(width)] for _ in range(height)]
        
        def move(cord):
            x, y = cord
                        
			# we stopped here before
            if marker[x][y]:
                return False
            
            if cord == destination:
                return True               
            
            marker[x][y] = True # marked
            
            r, l = y+1, y-1
            u, d = x-1, x+1
            
            # move to right wall or obstacle
            while r < width and maze[x][r] == 0:
                r += 1
            if move([x, r-1]):
                return True
            
            # move to left wall or obstacle
            while l >= 0 and maze[x][l] == 0:
                l -= 1
            if move([x, l+1]):
                return True
            
            # move upward
            while u >= 0 and maze[u][y] == 0:
                u -= 1
            if move([u+1, y]):
                return True
            
            # move downward
            while d < height and maze[d][y] == 0:
                d += 1
            if move([d-1, y]):
                return True
            
            return False

        return move(start)
            
            
        

        
        
#         class Solution:
#     def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
#         def dfs(r, c):
#             if r == destination[0] and c == destination[1]:
#                 return True
#             for dr, dc in (-1, 0), (0, 1), (1, 0), (0, -1):
#                 nr, nc = r, c
#                 while 0 <= nr + dr < m and 0 <= nc + dc < n and maze[nr + dr][nc + dc] != 1:
#                     nr += dr
#                     nc += dc
#                 if (nr, nc) not in visited:
#                     visited.add((nr, nc))
#                     if dfs(nr, nc):
#                         return True
#             return False

#         m, n = len(maze), len(maze[0])
#         visited = set()

#         return dfs(start[0], start[1])



