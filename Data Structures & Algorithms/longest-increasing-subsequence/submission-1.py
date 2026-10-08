class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        l = len(nums)

        dp = [0] * l
        dp[0] = 1

        for i in range(1, l):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j])
            
            dp[i] += 1
        
        return max(dp)