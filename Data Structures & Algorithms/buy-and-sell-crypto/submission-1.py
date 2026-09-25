class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        days = len(prices)

        lowest_buy_in = float('inf')

        for i in range(days):
            if not prices[i] < lowest_buy_in:
                continue
            else:
                lowest_buy_in = prices[i]
                for j in range(i+1, days):
                    res = max((prices[j] - lowest_buy_in), res)
            
        return res