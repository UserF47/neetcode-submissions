class Solution:
    def findMin(self, nums: List[int]) -> int:
        # For log(n) complexity we will go for binary search
        # what is the start and end index since the array was rotated at least once and at most n times.
        # how many cases we have for the array
        # rotate once: [7,1,2,3,4,5,6]
        # rotate 4 times: [4,5,6,7,0,1,2]
        # rotate n times: [1,2,3,4,5,6,7]
        # the min is less than both nums on its left and right
        # it should within a range where leftmost is larger than rightmost
        
        size = len(nums)
        # if nums[0] <= nums[size-1]:
        #     return nums[0]

        left = 0
        right = size - 1

        while left <= right:
            mid = (left+right)//2

            if nums[left] <= nums[right]:
                return nums[left]
            
            if nums[left] > nums[mid]:
                right = mid
            else:
                left = mid+1
