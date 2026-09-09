class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        count = n

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]

            return x

        for a, b in edges:
            root_a, root_b = find(a), find(b)
            if root_a == root_b:
                return False

            parent[root_a] = root_b
            count -= 1

        return (count == 1) 