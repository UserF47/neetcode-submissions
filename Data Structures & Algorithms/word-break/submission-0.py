class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        worldDictSet = set(wordDict)
        dp = [False] * (len(s) + 1)

        dp[0] = True

        for i in range(1, len(s)+1):
            for j in range(0, i):
                if dp[j] == True and s[j: i] in worldDictSet:
                    dp[i] = True
                    break
        
        return dp[len(s)]
                    