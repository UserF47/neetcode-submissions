# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        counter = 1
        res = None

        def dfs(node):
            nonlocal counter, res

            if not node or res is not None:
                return
            
            dfs(node.left)
            if counter == k:
                res = node.val
            
            counter += 1
            dfs(node.right)

            return
            
        dfs(root)
        
        return res