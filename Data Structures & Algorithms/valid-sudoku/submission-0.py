class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row=defaultdict(set)
        col=defaultdict(set)
        cell=defaultdict(set)

        for i in range(0, 9):
            for j in range(0, 9):
                r = i // 3
                c = j // 3
                ce = str(r) + str(c)
                
                if board[i][j] == ".":
                    continue

                num = int(board[i][j])

                if num in row[i]:
                    return False
                else:
                    row[i].add(num)

                if num in col[j]:
                    return False
                else:
                    col[j].add(num)

                if num in cell[ce]:
                    return False
                else:
                    cell[ce].add(num)
        
        return True