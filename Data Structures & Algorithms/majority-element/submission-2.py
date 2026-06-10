class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res = {}
        max = 0 
        element = 0
        for i in range(len(nums)):
            if nums[i] not in res:
                res[nums[i]] = 1
            else:
                res[nums[i]] += 1
            
        for i in range(len(nums)):
            if res[nums[i]] > max :
                max = res[nums[i]]
                element = nums[i]

        return element