class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if digits == "":
            return []
        letterMap = [
            "",
            "",
            "abc",
            "def",
            "ghi",
            "jkl",
            "mno",
            "pqrs",
            "tuv",
            "wxyz",
        ]
        def backtrack(index, digits, path):
            if index == len(digits):
                res.append(path)
                return
            #convert char to index
            letters = letterMap[int(digits[index])]
            for i in range(len(letters)):
                path += letters[i]
                backtrack(index + 1, digits, path)
                path = path[:-1]
        backtrack(0,digits, "")
        return res