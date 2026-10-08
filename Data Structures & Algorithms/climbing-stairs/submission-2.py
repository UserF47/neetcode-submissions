class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1

        prev_2 = 1
        prev_1 = 2

        for _ in range(3, n+1):
            cur = prev_2 + prev_1
            prev_2 = prev_1
            prev_1 = cur
        
        return prev_1