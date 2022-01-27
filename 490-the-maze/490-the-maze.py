class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        rows = len(maze)
        cols = len(maze[0])
        visited = set()

        def dfs(row, col):
            
            if (row,col) in visited: return False
            if [row,col] == destination: return True
            visited.add((row,col))
            
            right, left = col + 1, col - 1
            up, down = row - 1, row + 1
            #move right until obstacle
            while right < cols and maze[row][right] == 0:
                
                right += 1
            if dfs(row, right -1): return True
                
            #move left
            while left >= 0 and maze[row][left] == 0:
                
                left -= 1
            if dfs(row, left + 1): return True
                
            #move up
            while up >= 0 and maze[up][col] == 0:
                
                up -= 1
            if dfs(up + 1, col): return True
            #move down 
            while down < rows and maze[down][col] == 0:
                
                down += 1
            if dfs(down - 1, col): return True
                
        
        return dfs(*start)
            
            
        

        
        
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



