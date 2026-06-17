class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            first = nums[i]
            l = i + 1
            r = len(nums)-1

            while l<r:
                threesum = first + nums[l] + nums[r]
                if threesum > 0 :
                    r -= 1
                elif threesum <0 : 
                    l += 1
                else:
                    res.append([first,nums[l], nums[r]])
                l += 1
                r -= 1
                while l > 0 and nums[l] == nums[l-1] and l<r:
                    l += 1
        return res
        
        