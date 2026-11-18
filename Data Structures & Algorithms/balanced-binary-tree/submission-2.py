# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root):
            if not root:
                return 0, True
            
            h_l, res_l = dfs(root.left)
            h_r, res_r = dfs(root.right)

            if not res_l or not res_r:
                return 0, False

            if abs(h_l - h_r) > 1:
                return 0, False
            
            return 1 + max(h_l, h_r), True
        
        _, res = dfs(root)

        return res
