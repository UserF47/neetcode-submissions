class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        length_text1, length_text2 = len(text1), len(text2)
        
        dp = []
        for _ in range(length_text1):
            row = [-1] * length_text2
            dp.append(row)

        def find_max_common(i, j):
            if i == length_text1 or j == length_text2:
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            if text1[i] == text2[j]:
                cur_length = 1 + find_max_common(i+1, j+1)
                dp[i][j] = cur_length
                return cur_length
            
            cur_length = max(find_max_common(i, j+1), find_max_common(i+1, j))
            dp[i][j] = cur_length

            return cur_length
        
        return find_max_common(0, 0)
