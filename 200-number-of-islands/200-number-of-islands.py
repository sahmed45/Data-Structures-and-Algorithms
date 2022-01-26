class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: return 0
        islands = 0
        visited = set()
        rows, cols = len(grid), len(grid[0])
 
        def dfs(grid, row, col):
            visited.add((row,col))
        #explore left
            if col > 0 and grid[row][col - 1] == "1" and (row,col - 1) not in visited:
                dfs(grid, row, col - 1)
        #explore right, cols - 1 because of index and length + 1 difference
            if col < cols - 1 and grid[row][col + 1] == "1" and (row,col + 1) not in visited:
                dfs(grid, row, col + 1)
        #explore up
            if row > 0 and grid[row - 1][col] == "1" and (row - 1,col) not in visited:
                dfs(grid, row - 1, col)
        #explore down
            if row < rows - 1 and grid[row + 1][col] == "1" and (row + 1,col) not in visited:
                dfs(grid, row + 1, col)


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    islands += 1
                    dfs(grid, row, col)
        return islands
                    
            
        
        
#         if not grid:
#             return 0
        
#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         islands = 0
        
#         def bfs(row,col):
#             q = deque()
#             q.append((row,col))
#             visited.add((row,col))
            
#             while q:
#                 r, c = q.popleft()
#                 #up, left, right, down
#                 directions = [[1,0], [-1,0], [0,1], [0, -1]]
                
#                 for dr, dc in directions:
#                     row, col = r + dr, c + dc
#                     #make sure neighbors are in range,
#                     #all neightboring 1's need to be added so no duplicate islands
#                     if (row in range(rows) and
#                         col in range(cols) and
#                         grid[row][col] == "1" and
#                         (row, col) not in visited):
#                         q.append((row, col))
#                         visited.add((row, col))
        
#         for row in range(rows):
#             for col in range(cols):
#                 #run bfs on each 1 to detect neighboring 1's
#                 if grid[row][col] == "1" and (row,col) not in visited:
#                     bfs(row,col)
#                     islands += 1
#         return islands