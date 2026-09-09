class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        pacific_cells = set()
        atlantic_cells = set()

        res = []

        #start from a cell find which cells it can reach
        def dfs(i, j, ocean):
            if (i, j) in ocean:
                return
            
            ocean.add((i, j))
            direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for change in direction:
                i_change, j_change = change

                if 0 <= i + i_change < rows and  0 <= j + j_change < cols and heights[i][j] <= heights[i + i_change][j + j_change]:
                    dfs(i + i_change, j + j_change, ocean)
                    

        #start from pacific ocean, find which cells it can reach, append to pacific_cells
        for i in range(rows):
            dfs(i, 0, pacific_cells)
        
        for j in range(1, cols):
            dfs(0, j, pacific_cells)

        #start from atlantic ocean, find which cells it can reach, append to atlantic_cells
        for i in range(0, rows):
            dfs(i, cols-1, atlantic_cells)
        
        for j in range(0, cols):
            dfs(rows-1, j, atlantic_cells)

        #get the intersected cells between those two
        for cell in pacific_cells:
            if cell in atlantic_cells:
                res.append(list(cell))

        return res