class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # [3,4,5,6,1,2]

        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: #left sorted
                if target > nums[mid]:
                        left = mid + 1
                else: # target < nums[mid]:
                    if target < nums[left]:
                        left = mid + 1
                    else: # target > nums[left]
                        right = mid - 1
            else: #right sorted
                if target < nums[mid]:
                        right = mid - 1
                else: # target > nums[mid]:
                    if target > nums[right]:
                        right = mid - 1
                    else: # target < nums[right]
                        left = mid + 1

        # nums=[3, 1]
        # target=1

        return -1 