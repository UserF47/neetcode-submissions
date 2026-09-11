class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        min_prod = nums[0]
        max_prod = nums[0]
        res = nums[0]

        for i in range(1, len(nums)):
            cur = [max_prod * nums[i], min_prod * nums[i], nums[i]]

            max_prod = max(cur)
            min_prod = min(cur)

            res = max(max_prod, res)

        return res