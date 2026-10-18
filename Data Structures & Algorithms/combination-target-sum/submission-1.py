nums = [2,5,6,9]
target = 9


class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        current_sum = 0

        def dfs(i):
            nonlocal current_sum
            if current_sum == target:
                res.append(path[:])
                return
            
            if i == len(nums):
                return
            
            if current_sum + nums[i] <= target:
                path.append(nums[i])
                current_sum += nums[i]
                dfs(i)
                path.pop()
                current_sum -= nums[i]

            dfs(i+1)

        dfs(0)

        return res
