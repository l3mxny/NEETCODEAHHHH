class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(r,c):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return
            #dont do anything
            if board[r][c] == "X":
                return
            #already visited, dont do anything
            if board[r][c] == "#":
                return
            #mark the borders first 
            board[r][c] = "#"
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        
        for c in range(len(board[0])):
            dfs(0,c)
            dfs(len(board)-1, c)
        for r in range(len(board)):
            dfs(r,0)
            dfs(r, len(board[0])-1)
        
        
        for r in range(len(board)):
            for c in range(len(board[0])):
                #actual turning O to X.
                if board[r][c] == "O":
                    board[r][c] = "X"
                #unblock the borders to show
                elif board[r][c] == "#":
                    board[r][c] = "O"


        