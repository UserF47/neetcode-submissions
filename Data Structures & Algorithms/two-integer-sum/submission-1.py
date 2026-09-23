class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h_map = dict()

        for i in range(len(nums)):
            if (target - nums[i]) in h_map:
                return [h_map[target - nums[i]], i]
            
            h_map[nums[i]] = i