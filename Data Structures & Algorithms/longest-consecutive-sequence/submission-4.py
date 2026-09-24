class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_len = 0

        nums_set = set(nums)
        visited = set()
        
        for num in nums:
            if not num in visited:
                counter = 1
                visited.add(num)

                while (num + 1) in nums_set:
                    counter += 1
                    num += 1
                    visited.add((num + 1))
                
                max_len = max(max_len, counter)
        
        return max_len

