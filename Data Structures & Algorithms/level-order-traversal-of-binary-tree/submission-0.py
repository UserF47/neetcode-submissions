# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q = deque([root])
        res = []

        while q:
            level = []
            q2 = deque()

            while q:
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q2.append(node.left)
                
                if node.right:
                    q2.append(node.right)

            res.append(level)
            
            while q2:
                node = q2.popleft()
                q.append(node)

        return res
