class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        path = []

        cur_sum = 0
        candidates.sort()

        def dfs(path_index):
            nonlocal cur_sum
            
            if cur_sum == target:
                res.append(path[:])
                return
            
            if path_index == len(candidates):
                return 
            
            if cur_sum + candidates[path_index] > target:
                return

            path.append(candidates[path_index])
            cur_sum += candidates[path_index]

            dfs(path_index+1)

            path.pop()
            cur_sum -= candidates[path_index]
            
            next_index = path_index+1
            while next_index < len(candidates) and candidates[next_index] == candidates[path_index]:
                next_index += 1
            dfs(next_index)

            return
        
        dfs(0)

        return res
            
