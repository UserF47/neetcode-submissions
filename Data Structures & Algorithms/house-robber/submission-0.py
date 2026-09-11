class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        prev_2 = nums[0]
        prev_1 = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            cur = max(prev_1, prev_2 + nums[i])
            prev_2 = prev_1
            prev_1 = cur
        
        return prev_1