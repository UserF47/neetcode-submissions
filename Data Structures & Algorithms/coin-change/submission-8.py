class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp array 0 -> amount, coins = [2]
        # index 0, 1, 2, 3, 4
        # #coin -1, -1, 2, 3, 4, 1, 2, 3, 4, 5, 1, 2, 3
        if amount == 0:
            return 0

        dp = [-1] * (amount + 1)
        
        dp[0] = 0
        dp[1] = 1 if 1 in coins else -1

        for i in range(2, (amount + 1)):
            num_coins = float('inf')
            for c in coins:
                if i-c >= 0 and dp[i-c] != -1:
                    num_coins = min(1 + dp[i-c], num_coins)
                    
            dp[i] = num_coins if num_coins != float('inf') else -1
        
        return dp[-1]