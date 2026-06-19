class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        #called upon on land 
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                #it is a land
                return 1
            #neighboring water
            if grid[r][c] == 0: 
                return 1
            if grid[r][c] == 2:
                return 0 
            grid[r][c] = 2
            return dfs(r-1,c) + dfs(r+1,c) + dfs(r,c+1) + dfs(r,c-1)           

        #loop through grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #start dfs on land
                if grid[i][j] == 1:
                    return dfs(i,j)