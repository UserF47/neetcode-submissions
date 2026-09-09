class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        latest_low = prices[0] 
        max_profit = 0

        for i in range(1, len(prices)):
            max_profit = max(prices[i]-latest_low, max_profit)
            latest_low = min(prices[i], latest_low)
        
        return max_profit