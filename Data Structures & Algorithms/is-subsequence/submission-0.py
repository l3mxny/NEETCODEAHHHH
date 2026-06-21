class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #needs order
        l = 0 
        r = 0 

        while l < len(s):
            while r < len(t) and s[l] != t[r]:
                r += 1
                #reached end. nothing to compare next
                if r == len(t)-1:
                    return False
            l += 1
            r += 1
            
        return True