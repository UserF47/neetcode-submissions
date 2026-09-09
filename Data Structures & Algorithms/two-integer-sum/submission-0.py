class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in visited:
                return [visited[rest], i]
            else:
                visited[nums[i]] = i