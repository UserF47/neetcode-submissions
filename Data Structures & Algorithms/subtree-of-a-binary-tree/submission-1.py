# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def isSameTree(node_1, node_2):
            if not node_1 or not node_2:
                if not node_1 and not node_2:
                    return True
                else:
                    return False
            
            if node_1.val != node_2.val:
                return False
            
            return isSameTree(node_1.left, node_2.left) and isSameTree(node_1.right, node_2.right)

        
        def dfs(node_1, node_2):
            if not node_1:
                return False
            
            if isSameTree(node_1, node_2):
                return True
            
            return dfs(node_1.left, node_2) or dfs(node_1.right, node_2)
        
        return dfs(root, subRoot)
            






