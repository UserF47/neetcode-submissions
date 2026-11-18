# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(root):
            nonlocal res
            
            if not root:
                return 0
            
            len_left = dfs(root.left)
            len_right = dfs(root.right)
            res = max(res, (len_left + len_right))

            return 1 + max(len_left, len_right)
        
        dfs(root)

        return res