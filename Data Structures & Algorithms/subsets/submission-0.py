# given a list: [1, 2]
# [[],[1],[2],[1,2]]

# nums = [1,2,3]
# [1, 2, 3]
# [1, 2]
# [1, 3]

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def dfs(i):
            if i == len(nums):
                res.append(path[:])
                return

            # choose current number:
            path.append(nums[i])
            dfs(i+1)
            path.pop()

            # not choose current number
            dfs(i+1)
        
        dfs(0)

        return res