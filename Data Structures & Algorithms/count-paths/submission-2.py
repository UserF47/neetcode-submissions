class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = []
        for _ in range(m):
            row = [0] * n
            dp.append(row)

        def dfs_find_path(i, j):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if dp[i][j] != 0:
                return dp[i][j]

            cur_path = dfs_find_path(i+1, j) + dfs_find_path(i, j+1)
            dp[i][j] = cur_path

            return cur_path
        
        return dfs_find_path(0, 0)
        