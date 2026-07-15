class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = {}

        def dfs(i):
            if i >= n:
                return 0 
            elif i in memo:
                #get cached value
                return memo[i]
            else: 
                #add up all steps 
                memo[i]= cost[i] + min(dfs(i+1), dfs(i+2))
            return memo[i]
        #start from positions 0 and 1
        return min(dfs(0),dfs(1))
        