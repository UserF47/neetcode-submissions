# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        max_diameter = float('-inf')

        def getDiameter(node):
            nonlocal max_diameter

            if not node:
                return 0

            left_d = getDiameter(node.left)
            right_d = getDiameter(node.right)

            max_diameter = max(max_diameter, left_d + right_d)

            return max(left_d, right_d) + 1

        getDiameter(root)

        return max_diameter
