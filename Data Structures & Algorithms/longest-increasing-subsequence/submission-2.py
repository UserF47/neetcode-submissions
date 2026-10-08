class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)

        dp = [1] * l

        for i in range(1, l):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)