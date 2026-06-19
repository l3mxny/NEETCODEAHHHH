class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()


        def backtrack(r,c,i):
            if r < 0 or r >= len(board) or c < 0 or c >= len(board[0]):
                return False
            if (r,c) in visited: 
                return False
            if i == len(word):
                return True
            if board[r][c] != word[i]:
                return False
            
            visited.add((r,c))
            down = backtrack(r+1,c,i+1)
            up = backtrack(r-1,c,i+1)
            left = backtrack(r,c-1,i+1)
            right = backtrack(r,c+1,i+1)
            res = down or up or left or right
            visited.remove((r,c))
            return res
        

        for r in range(len(board)):
            for c in range(len(board[0])):
                if backtrack(r,c,0):
                    return True
        return False
   
