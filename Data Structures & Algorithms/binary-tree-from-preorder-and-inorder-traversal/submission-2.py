# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos = {val: index for index, val in enumerate(inorder)}
        pre = 0

        def build(low, high):
            nonlocal pre

            if low > high:
                return None
            
            root = TreeNode(preorder[pre])
            pre += 1
            mid = pos[root.val]

            root.left = build(low, mid-1)
            root.right = build(mid+1, high)

            return root

        return build(0, len(preorder) - 1)




