class Solution:
    #call on two seperate slices of array on house robber I
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        else:
            return max(self.robCircle(nums[0:len(nums)-1]), self.robCircle(nums[1:len(nums)]))
    def robCircle(self, nums: List[int]) -> int:
        memo = {}
        n = len(nums)
        def dfs(i):
            if i >= n:
                return 0 
            elif i in memo:
                return memo[i]
            else:
                memo[i] =  max(dfs(i+1), nums[i] + dfs(i+2))
            return memo[i]
        return dfs(0)
           

        