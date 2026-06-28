class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        pacific = set()
        atlantic = set()
        
        def dfs(r,c,visit, prevHeight):
            if r < 0 or r >= len(heights) or c < 0 or c >= len(heights[0]):
                return
            if (r,c) in visit:
                return 
            if heights[r][c] < prevHeight:
                return
            visit.add((r,c))
            #explore neighbors
            dfs(r+1,c,visit,heights[r][c])
            dfs(r-1,c,visit,heights[r][c])
            dfs(r,c-1,visit,heights[r][c])
            dfs(r,c+1,visit,heights[r][c])
        #starting from borders
        
        for c in range(len(heights[0])):
            dfs(0, c, pacific, heights[0][c])
            dfs(len(heights) - 1, c, atlantic, heights[len(heights) - 1][c])
        for r in range(len(heights)):
            dfs(r, 0, pacific, heights[r][0])
            dfs(r, len(heights[0]) - 1, atlantic, heights[r][len(heights[0]) - 1])

        res = []
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if (r,c) in pacific and (r,c) in atlantic:
                    res.append([r,c])
        return res
