class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [i for i in range(len(edges)+1)]

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            
            return x
        
        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a != root_b:
                parent[root_a] = root_b
            else:
                return [a, b]
        
        # return count
        