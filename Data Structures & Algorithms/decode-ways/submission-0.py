class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def dfs(i):
            if i == len(s):
                return 1
            #no start with 0
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]
            ways = dfs(i+1)
            num = int(s[i: i+2])
            #for double digits
            if num >= 10 and num <= 26:
                ways2 = dfs(i+2)
            else:
                ways2 = 0 
            #cache the summed values
            memo[i] = ways + ways2
            return memo[i]
        return dfs(0)