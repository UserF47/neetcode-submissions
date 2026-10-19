class Solution:
    def jump(self, nums: List[int]) -> int:
        num_of_nums = len(nums)
        dp = [float('inf')] * num_of_nums
        dp[num_of_nums-1] = 0

        for i in range(num_of_nums-2, -1, -1): #each position i
            for j in range(i+1, min(num_of_nums, i+nums[i]+1)): #legal reachable positions from i
                dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[0]