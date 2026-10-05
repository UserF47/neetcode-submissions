from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0
        changed = True

        rows = len(grid)
        cols = len(grid[0])

        num_fresh = 0

        rotten = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    num_fresh += 1
                
                if grid[r][c] == 2:
                    rotten.append((r, c))

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        while rotten and num_fresh:
            for _ in range(len(rotten)):
                r, c = rotten.popleft()
                for d in directions:
                    if 0 <= r+d[0] < rows and 0 <= c+d[1] < cols and grid[r+d[0]][c+d[1]]==1:
                        grid[r+d[0]][c+d[1]] = 2
                        rotten.append((r+d[0], c+d[1]))
                        num_fresh -= 1
            minutes += 1
        
        return -1 if num_fresh else minutes










