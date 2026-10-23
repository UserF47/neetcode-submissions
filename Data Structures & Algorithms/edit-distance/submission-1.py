class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length_word1, length_word2 = len(word1), len(word2)

        dp = []
        for _ in range(length_word1+1):
            row = [-1] * (length_word2+1)
            dp.append(row)

        def get_min_distance(i, j):
            if dp[i][j] != -1:
                return dp[i][j]

            if i == length_word1:
                dp[i][j] = length_word2 - j
                return length_word2 - j
            
            if j == length_word2:
                dp[i][j] = length_word1 - i
                return length_word1 - i
            
            if word1[i] == word2[j]:
                min_distance = get_min_distance(i+1, j+1)
                dp[i][j] = min_distance
                return min_distance

            min_distance = 1 + min(get_min_distance(i+1, j+1), get_min_distance(i, j+1), get_min_distance(i+1, j))
            dp[i][j] = min_distance
            return min_distance

        return get_min_distance(0, 0)
