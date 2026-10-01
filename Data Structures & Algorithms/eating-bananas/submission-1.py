class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left = 1
        right = max(piles)
        res = float('inf')

        while left <= right:
            rate = (left+right) // 2

            hours = 0
            for pile in piles:
                hours += (pile + rate - 1) // rate
            
            if hours > h:
                left = rate + 1
            else:
                res = min(res, rate)
                right = rate - 1
        
        return res
            

        
