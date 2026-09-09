# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        in_order_index = {val:idx for idx, val in enumerate(inorder)}
        root_index = 0

        def build(left, right):
            nonlocal root_index
            if left > right:
                return None

            root_cur = preorder[root_index]
            root_cur_node = TreeNode(root_cur)
            
            root_in_in_order = in_order_index[root_cur]

            root_index += 1

            root_cur_node.left = build(left, root_in_in_order-1)
            root_cur_node.right = build(root_in_in_order+1, right)

            return root_cur_node
        
        return build(0, len(preorder)-1)