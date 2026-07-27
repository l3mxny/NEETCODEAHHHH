class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curMin = 1
        curMax = 1
        res = float('-inf')
        for num in nums: 
            conditions = (num, curMin * num, curMax * num)
            curMin = min(conditions)
            curMax = max(conditions)
            #update only the max
            res = max(res,curMax)
        return res
        