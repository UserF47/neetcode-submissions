class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        length_nums = len(nums)
        dp_hashmap = {}

        def dfs(i, target):
            if i == length_nums:
                if target == 0:
                    return 1
                else:
                    return 0

            if (i, target) in dp_hashmap:
                return dp_hashmap[(i, target)]

            cur = dfs(i+1, target - nums[i]) + dfs(i+1, target + nums[i])
            dp_hashmap[(i, target)] = cur
            
            return cur
        
        return dfs(0, target)