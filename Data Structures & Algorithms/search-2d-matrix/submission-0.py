class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # m row, n cols
        # i = 0, j = m*n - 1, mid = (i+j)//2
        # mid // n -> row
        # mid % n -> col
        # example 1: i = 0, j = 11, mid = 5, m=3, n=4, mid at row 1, col 1 -> 11

        m = len(matrix) # #rows
        n = len(matrix[0]) # #cols

        i, j = 0, m*n-1

        while i <= j:
            mid = (i+j) // 2
            mid_val = matrix[mid//n][mid%n]

            if mid_val == target:
                return True
            elif mid_val < target:
                i = mid + 1
            else:
                j = mid - 1
        
        return False
