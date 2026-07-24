class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        count = 0
        dp = [[False] * n for _ in range(n)]
        #starts from outside of diagnoal matrix and goes in
        for i in range(n-1,-1,-1):
            for j in range(i,n):
                #outer then go in and check 
                if s[i] == s[j] and (j-i <= 2 or dp[i+1][j-1]):
                    dp[i][j] = True
                    count += 1
        return count