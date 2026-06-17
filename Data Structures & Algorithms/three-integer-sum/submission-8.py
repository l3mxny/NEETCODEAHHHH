class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        i = 0 
        for i in range(len(nums)):
            first = nums[i]
            #skip dupe numbers of first
            if i > 0 and first == nums[i-1]:
                continue

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
                #skips dupe of second number
                while l<r and nums[l] == nums[l-1]:
                    l += 1
           
        return res
        
        