class Solution:
    def isHappy(self, n: int) -> bool:
        num = n 
        seen = set()
        newNum = 0 

        while num != 1:
            seen.add(num)
            while num > 0:
                digit = num % 10 
                newNum += digit * digit
                num //= 10
            num = newNum
            newNum = 0 
            if num in seen:
                return False
        return True
        