class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0 
        maxCount = 0 
        for i in range(len(nums)):
            if nums[i] == 0:
                maxCount = max(maxCount,count)
                count = 0 
            else:
                count += 1
        return max(maxCount,count)
        