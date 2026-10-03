# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        last = float('-inf')
        res = True

        def bfs(node):
            nonlocal last, res

            if not node:
                return 
            
            bfs(node.left)

            if node.val > last:
                last = node.val
            else:
                res = False
                return
            
            bfs(node.right)
        
        bfs(root)

        return res