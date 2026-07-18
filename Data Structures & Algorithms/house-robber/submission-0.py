class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def dfs(i):
            if i >= n:
                return 0
            elif i in memo:
                return memo[i]
            else:
                #skip house i, move step forward; rob house i , gain nums[i] and skip adjacent one
                memo[i] =  max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
        return dfs(0)