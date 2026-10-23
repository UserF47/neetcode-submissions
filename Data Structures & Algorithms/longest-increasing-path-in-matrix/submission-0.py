class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        rows = len(matrix)
        cols = len(matrix[0])

        dp = []
        for _ in range(rows):
            row = [-1] * (cols)
            dp.append(row)

        def get_longest_increasing_path(i, j):
            # if i == rows or j == cols:
            #     return 0
            
            if dp[i][j] != -1:
                return dp[i][j]
            
            longest_next_step = 0

            if (i+1) < rows and matrix[i+1][j] > matrix[i][j]:
                longest_next_step = max(longest_next_step, get_longest_increasing_path(i+1, j))
            

            if (i-1) > -1 and matrix[i-1][j] > matrix[i][j]:
                longest_next_step = max(longest_next_step, get_longest_increasing_path(i-1, j))
            

            if (j+1) < cols and matrix[i][j+1] > matrix[i][j]:
                longest_next_step = max(longest_next_step, get_longest_increasing_path(i, j+1))
            

            if (j-1) > -1 and matrix[i][j-1] > matrix[i][j]:
                longest_next_step = max(longest_next_step, get_longest_increasing_path(i, j-1))
            
            dp[i][j] = 1 + longest_next_step
            
            return 1 + longest_next_step


        longest_path = 0
        for i in range(rows):
            for j in range(cols):
                longest_path = max(longest_path, get_longest_increasing_path(i, j))
        
        return longest_path
            
