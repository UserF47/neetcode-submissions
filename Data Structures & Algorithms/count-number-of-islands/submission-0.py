class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0

        rows = len(grid)
        cols = len(grid[0])
        
        def dfs(i, j):
            if i < 0 or i >= rows or j < 0 or j >= cols or grid[i][j]=='0':
                return
            
            grid[i][j] = '0'

            dfs(i-1, j)
            dfs(i, j-1)
            dfs(i+1, j)
            dfs(i, j+1)

            return

        for i in range(0, rows):
            for j in range(0, cols):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)
        
        return count
