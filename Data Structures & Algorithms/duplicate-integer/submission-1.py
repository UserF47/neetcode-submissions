class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h_set = set()

        for num in nums:
            if num in h_set:
                return True
        
            h_set.add(num)
        
        return False