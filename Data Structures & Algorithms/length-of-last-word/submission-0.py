class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        left = len(s) - 1
        right = len(s) - 1
        while s[left] == " ":
            right -= 1
            left -= 1
        while s[left] != " " and left >= 0 :
            left -= 1 
        return right - left 