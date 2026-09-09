# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSameTree(self, rootA, rootB):
        if (not rootA) or (not rootB):
            return (not rootA) and (not rootB)

        if rootA.val != rootB.val:
            return False
        
        leftRes = self.isSameTree(rootA.left, rootB.left)
        rightRes = self.isSameTree(rootA.right, rootB.right)

        return (leftRes and rightRes)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        res = False

        def dfs(root, subroot):
            nonlocal res

            if not root:
                return
            
            if self.isSameTree(root, subroot):
                res = True
            
            dfs(root.left, subroot)
            dfs(root.right, subroot)
        
        dfs(root, subRoot)

        return res
        