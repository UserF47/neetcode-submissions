class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0

        nums_set = set(nums)
        
        for num in nums:
            if not (num-1) in nums_set:
                counter = 1

                while (num + 1) in nums_set:
                    counter += 1
                    num += 1
                
                max_len = max(max_len, counter)
        
        return max_len

