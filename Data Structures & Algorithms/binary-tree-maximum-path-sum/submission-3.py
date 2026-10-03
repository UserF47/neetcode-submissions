# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = float('-inf')

        def dfs(node):
            nonlocal res

            if not node:
                return 0
            
            sum_left = dfs(node.left)
            sum_right = dfs(node.right)

            current = node.val
            if sum_left > 0:
                current += sum_left
            
            if sum_right > 0:
                current += sum_right
            
            res = max(current, res)

            return max(node.val, node.val+sum_left, node.val+sum_right)
        
        dfs(root)

        return res