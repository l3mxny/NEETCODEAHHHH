class Solution:
    def isPalindrome(self, x: int) -> bool:
        res = str(x)
        compare = res[::-1]
        if x < 0:
            return False
        elif res == compare:
            return True
        return False