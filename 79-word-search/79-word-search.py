class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        #to not use same letter more than once
        path = set()
        directions = [(-1,0),(1,0),(0,-1),(0,1)]
        
        def dfs(row,col, count):
            if count == len(word): return True
            
            if (row < 0 or row >= rows or col < 0 or 
                col >= cols or word[count] != board[row][col] or 
               (row, col) in path):
                return False
            
            path.add((row,col))
            
            for dr, dc in directions:
                if dfs(row + dr, col + dc, count + 1): return True
            
            path.remove((row,col))
            
        
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if dfs(row,col, 0): return True
        return False
            
        