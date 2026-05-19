#mysolution
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dict={}
        for i in range(9):
            row = set()
            #rows, check rows first then 3x3 in 9x9
            for j in range(9):
                if board[i][j] == '.':
                    continue;
                if board[i][j] not in row:
                    row.add(board[i][j])
                else: 
                    return False
                #3x3 boxes
                inside = dict.get((i//3,j//3), set())
                if board[i][j] in inside: 
                    return False
                #invalid
                else:
                    inside.add(board[i][j])
                    dict[(i//3,j//3)] = inside
            #col
            col = set()
            for k in range(9):
                if board[k][i] == '.':
                    continue;
                if board[k][i] not in col:
                    col.add(board[k][i])
                else:
                    return False
        return True

