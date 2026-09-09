# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        res = []

        def dfs(node):
            nonlocal res

            if not node:
                res.append('#')
                return
            
            res.append(str(node.val))
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        values = data.split(',')
        index = 0
        length = len(data)
        
        def dfs():
            nonlocal index
            val = values[index]
            index += 1

            if val == '#':
                return None

            node = TreeNode(int(val))

            node.left = dfs()
            node.right = dfs()

            return node
        
        root = dfs()

        return root