class Solution:
    def longestPalindrome(self, s: str) -> str:
        resLen = 0 
        resIndex = 0 

        #odd
        for i in range(len(s)):
            l = i 
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    resIndex = l
                l -= 1
                r += 1
        #even
        for i in range(len(s)):
            #stays even
            l = i
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r-l+1) > resLen:
                    resLen = r-l+1
                    #get left boundary
                    resIndex = l
                l -= 1
                r += 1
        #slice the palindrome
        return s[resIndex : resIndex + resLen]
