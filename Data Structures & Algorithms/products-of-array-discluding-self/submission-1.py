class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1] * len(nums)
        backward = [1] * len(nums)
        forward[0] = nums[0]
        backward[-1] = nums[-1]

        for i in range(1, len(nums)):
            forward[i] = forward[i-1] * nums[i]
        
        for i in range(len(nums)-2, -1, -1):
            backward[i] = backward[i+1] * nums[i]
        
        res = []
        res.append(backward[1])
        for i in range(1, len(nums)-1):
            # [1,2,3,4,5] len = 5 forward = 1 backward = 2 
            # [1,2,3,4,5] len = 5 forward = 2 backward = 1
            res.append(forward[i-1]*backward[i+1])
        res.append(forward[-2])

        return res