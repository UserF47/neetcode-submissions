# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        counter = 0

        def dfs(node, max_so_far):
            nonlocal counter

            if not node:
                return
            
            if node.val >= max_so_far:
                counter += 1
                max_so_far = node.val
            
            dfs(node.left, max_so_far)
            dfs(node.right, max_so_far)
        
        dfs(root, root.val)

        return counter
