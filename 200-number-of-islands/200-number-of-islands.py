class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(row,col):
            q = deque()
            q.append((row,col))
            visited.add((row,col))
            
            while q:
                r, c = q.popleft()
                #up, left, right, down
                directions = [[1,0], [-1,0], [0,1], [0, -1]]
                
                for dr, dc in directions:
                    row, col = r + dr, c + dc
                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col] == "1" and
                        (row, col) not in visited):
                        q.append((row, col))
                        visited.add((row, col))
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and (row,col) not in visited:
                    bfs(row,col)
                    islands += 1
        return islands