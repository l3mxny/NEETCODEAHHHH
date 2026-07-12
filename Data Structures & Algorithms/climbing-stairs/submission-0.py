class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def rec(i):
            if i > n:
                #went too far
                return 0 
            if i == n:
                #one way reached to the top
                return 1
            if i in memo:
                #is the step in the cache, return # of steps at that step
                return memo[i]
            #recurse
            memo[i] = rec(i+1) + rec(i + 2)
            return memo[i]
        return rec(0)
            
            
        