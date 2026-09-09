class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() #nlong(n), n is the length of nums

        size = len(nums)
        res = set()

        for i in range(size):
            if nums[i] > 0:
                break
                
            if i  > 0 and nums[i-1] == nums[i]:
                continue

            target = -nums[i]

            j = i + 1
            k = size - 1

            while j < k:
                if nums[j] + nums[k] == target:
                    res.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    j += 1
                    k -= 1
                    while j < k and nums[j] == nums[j-1]:
                        j += 1
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1
                elif nums[j] + nums[k] > target:
                    k -= 1
                else:
                    j += 1
        
        return list(res)