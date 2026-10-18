# nums = [1,2,3]
# choice = 1 used= [1]
# choice = 2 used= [1, 2]
# choice = 3 used= [1, 2, 3]

# choice = 3 used= [1, 3, 2]

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = []

        def backtracking(start_index):
            if start_index == len(nums):
                res.append(used[:])
                return

            for choice in nums:
                if choice not in used:
                    used.append(choice)
                    backtracking(start_index+1)
                    used.pop()
            
            return
        
        backtracking(0)

        return res

