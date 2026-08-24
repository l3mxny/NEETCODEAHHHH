class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0 
        curEnd = 0 
        farthest = 0 

        for i in range(0,len(nums)-1):
            farthest = max(farthest, i + nums[i])
            if i == curEnd:
                res += 1
                curEnd = farthest
        return res
        