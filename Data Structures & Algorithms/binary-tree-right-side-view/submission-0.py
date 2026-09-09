# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        q = deque([root])
        res = []

        while q:
            level = []
            q_l = deque()

            while q:
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q_l.append(node.left)

                if node.right:
                    q_l.append(node.right)
            
            res.append(level[-1])

            while q_l:
                node = q_l.popleft()
                q.append(node)
        
        return res