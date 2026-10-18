class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        res = False

        visited = set()
        matching_letter_index = 0

        
        def dfs(row, col):
            nonlocal matching_letter_index, res

            if matching_letter_index == len(word):
                res = True
                return
            
            if row < 0 or col < 0 or row >= rows or col >= cols:
                return

            if (row, col) in visited:
                return

            directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

            if board[row][col] == word[matching_letter_index]:
                matching_letter_index += 1

                visited.add((row, col))

                for row_add, col_add in directions:
                    dfs(row + row_add, col + col_add)

                visited.remove((row, col))
                matching_letter_index -= 1
            
            return
        
        for i in range(rows):
            for j in range(cols):
                dfs(i, j)

        return res


            