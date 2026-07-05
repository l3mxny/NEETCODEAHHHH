class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = []
        l = 0 
        r = len(nums)-1
    
        def leftBoundary(l,r):
            resL = -1
            while l <= r:
                mid = l + (r-l) //2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid - 1
                else:
                    #keep searching left for very first index
                    resL = mid
                    r = mid - 1
            return resL

        
        def rightBoundary(l,r):
            resR = -1
            while l <= r:
                mid = l + (r-l) // 2
                if nums[mid] < target:
                    l = mid + 1
                elif nums[mid] > target:
                    r = mid -1
                else:
                    #keep searching right until very last index pos
                    resR = mid
                    l = mid + 1
            return resR
        
        res1=leftBoundary(l,r)
        res2=rightBoundary(l,r)

        res.append(res1)
        res.append(res2)
        return res
