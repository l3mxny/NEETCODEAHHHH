class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(index,path):
            if index == len(s):
                res.append(path.copy())
                return
            
            for end in range(index, len(s)):
                piece = s[index:end+1]
                #check backwards and forwards same
                if piece[::-1] == piece:
                    path.append(piece)
                    backtrack(end+1,path)
                    path.pop()
        backtrack(0,[])
        return res