class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums = set(nums)
        max_len = 0
        
        for num in nums:
            if (num - 1) in nums:
                continue
            
            cur = num
            cur_len = 1

            while cur+1 in nums:
                cur += 1
                cur_len += 1

            max_len = max(max_len, cur_len)

        return max_len