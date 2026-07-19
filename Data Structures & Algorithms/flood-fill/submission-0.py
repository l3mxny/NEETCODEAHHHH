class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        #get coordinates
        compare = image[sr][sc]
        #dont need to fill
        if compare == color:
            return image
        def dfs(r,c):
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]):
                return
            elif image[r][c] == compare:
                #change color
                image[r][c] = color
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c-1)
                dfs(r,c+1)
        dfs(sr,sc)
        return image