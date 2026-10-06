class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def money(num_list):
            if len(num_list) == 1:
                return nums[0]
            
            dp_1 = num_list[0]
            dp_2 = max(num_list[1], num_list[0])

            for i in range(2, len(num_list)):
                cur = max(num_list[i]+dp_1, dp_2)
                dp_1 = dp_2
                dp_2 = cur
            
            return dp_2
        
        return max(money(nums[:-1]), money(nums[1:]))
