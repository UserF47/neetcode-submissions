class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j):
            if not (0<=i<rows and 0<=j<cols and board[i][j] == 'O'):
                return
            
            board[i][j] = 'T'

            direction = [(-1,0),(1, 0), (0,-1), (0,1)]
            
            for d in direction:
                i_change, j_change = d
                dfs(i+i_change, j+j_change)

        for i in [0, rows-1]:
            for j in range(cols):
                if board[i][j] == 'O':
                    dfs(i, j)
        
        for j in [0, cols-1]:
            for i in range(1, rows-1):
                if board[i][j] == 'O':
                    dfs(i, j)
        
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                
                if board[i][j] == 'T':
                    board[i][j] = 'O'