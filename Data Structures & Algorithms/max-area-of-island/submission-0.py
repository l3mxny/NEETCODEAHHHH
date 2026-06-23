class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        res = 0 
        def dfs(r,c):
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]):
                return 0
            if grid[r][c] == 0:
                return 0
            if grid[r][c] == 1:
                grid[r][c] = 0
                #accumulate
                return 1 + dfs(r+1,c) + dfs(r-1,c) + dfs(r,c+1) + dfs(r,c-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    res = max(dfs(r,c),res)
        return res