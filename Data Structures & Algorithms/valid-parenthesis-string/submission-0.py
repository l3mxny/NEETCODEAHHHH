class Solution:
    def checkValidString(self, s: str) -> bool:
        leftStack = []
        starStack = []
        res = []

        for i in range(len(s)):
            if s[i] == '(':
                leftStack.append(i)
            elif s[i] == ')':
                if leftStack:
                    leftStack.pop()
                elif starStack:
                    starStack.pop()
                else:
                    return False
            else:
                starStack.append(i)
        while leftStack and starStack:
            leftIndex = leftStack.pop()
            starIndex = starStack.pop()
            if leftIndex > starIndex:
                return False
            else:
                continue
        return len(leftStack) == 0

        