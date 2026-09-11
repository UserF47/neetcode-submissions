class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_helper(nums_clip):
            if len(nums_clip) == 1:
                return nums_clip[0]

            prev_2 = nums_clip[0]
            prev_1 = max(nums_clip[0], nums_clip[1])

            for i in range(2, len(nums_clip)):
                cur = max(prev_1, prev_2 + nums_clip[i])
                prev_2 = prev_1
                prev_1 = cur
            
            return prev_1
        
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))