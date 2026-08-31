class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        row = len(matrix)
        col = len(matrix[0])
        topTemp = True
        leftTemp = True
        #save OG 
        for r in range(row):
            if matrix[r][0] == 0:
                leftTemp = False
        for c in range(col):
            if matrix[0][c] == 0:
                topTemp = False
        #mark 
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0 
                    matrix[0][c] = 0 
        #apply
        for r in range(1,row):
            for c in range(1,col):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0 
        #modify first col and row
        if not topTemp:
            for c in range(col):
                matrix[0][c] = 0 
        if not leftTemp:
            for r in range(row):
                matrix[r][0] = 0 
        


        
        