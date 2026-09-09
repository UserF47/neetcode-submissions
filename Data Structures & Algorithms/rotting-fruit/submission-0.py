class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rotten_oranges = deque()
        num_fresh_oranges = 0
        elapse_time = 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    num_fresh_oranges += 1
                
                if grid[i][j] == 2:
                    rotten_oranges.append((i, j))
        
        while rotten_oranges:
            next_round_rotten_ones = deque()

            while rotten_oranges:
                i, j = rotten_oranges.popleft()

                if grid[i][j] == 2:
                    if i-1>=0 and grid[i-1][j] == 1:
                        grid[i-1][j] = 2
                        next_round_rotten_ones.append((i-1, j))
                        num_fresh_oranges -= 1
                    
                    if i+1<rows and grid[i+1][j] == 1:
                        grid[i+1][j] = 2
                        next_round_rotten_ones.append((i+1, j))
                        num_fresh_oranges -= 1
                
                    if j-1>=0 and grid[i][j-1] == 1:
                        grid[i][j-1] = 2
                        next_round_rotten_ones.append((i, j-1))
                        num_fresh_oranges -= 1
                    
                    if j+1<cols and grid[i][j+1] == 1:
                        grid[i][j+1] = 2
                        next_round_rotten_ones.append((i, j+1))
                        num_fresh_oranges -= 1
                        
            if next_round_rotten_ones:
                elapse_time += 1

            while next_round_rotten_ones:
                rotten_oranges.append(next_round_rotten_ones.popleft())
        
        if num_fresh_oranges == 0:
            return elapse_time
        
        return -1