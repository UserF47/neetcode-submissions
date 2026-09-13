class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 != 0:
            return False
        
        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:
            for test_new in range(target, num - 1, -1):
                if dp[test_new - num]:
                    dp[test_new] = True
        
        return dp[target]