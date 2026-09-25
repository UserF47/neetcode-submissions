class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0
        lowest_buy_in = float('inf')

        for p in prices:
            lowest_buy_in = min(lowest_buy_in, p)
            res = max(res, (p-lowest_buy_in))
        
        return res