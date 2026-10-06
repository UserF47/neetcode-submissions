# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        def getHeight(node):
            nonlocal res

            if not node or not res:
                return 0
            
            left_height = getHeight(node.left)
            right_height = getHeight(node.right)
            diff = abs(left_height - right_height)
            if diff > 1:
                res = False
                return 0
            
            return max(left_height, right_height) + 1
        
        getHeight(root)

        return res
