class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        total_pare = n * 2

        open_pare = end_pare = 0

        path = []

        def dfs(pare_index):
            nonlocal open_pare, end_pare

            if open_pare > n or end_pare > open_pare:
                return

            if pare_index == total_pare:
                res.append(''.join(path))
                return
            
            path.append('(')
            open_pare += 1
            dfs(pare_index+1)
            path.pop()
            open_pare -= 1

            path.append(')')
            end_pare += 1
            dfs(pare_index+1)
            path.pop()
            end_pare -= 1
        
        dfs(0)

        return res

