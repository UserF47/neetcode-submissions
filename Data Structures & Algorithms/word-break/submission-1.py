class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        l = len(s)

        dp = [False] * (l+1)
        dp[0] = True

        for i in range(1, l+1):
            for w in wordDict:
                if i-len(w) >= 0 and s[i-len(w):i] == w and dp[i-len(w)]:
                    dp[i] = True
        
        return dp[l]
                    