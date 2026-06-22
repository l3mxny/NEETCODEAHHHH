class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return []
        #dict
        letterMap = {
            "0":"",
            "1":"",
            "2": "abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }
        def backtrack(index, digits, path):
            if index == len(digits):
                res.append(path)
                return
            
            letters = letterMap[(digits[index])]
            for i in range(len(letters)):
                path += letters[i]
                backtrack(index + 1, digits, path)
                path = path[:-1]
        backtrack(0,digits, "")
        return res