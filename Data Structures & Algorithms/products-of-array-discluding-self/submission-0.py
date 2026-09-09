class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        forward = [1] * length
        cur = 1

        for i in range(1, length):
            forward[i] = forward[i-1] * nums[i-1]

        for i in range(length-2, -1, -1):
            cur = cur * nums[i+1]
            forward[i] *= cur

        return forward       