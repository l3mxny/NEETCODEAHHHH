#after finding the pivot position, search for target based on which half
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0 
        r = len(nums)-1
        while l < r:
            mid = l + (r-l) // 2
            if nums[mid] > nums[r]:
                l = mid + 1
            else:
                r = mid
        #exit with l == r, both pointers pointing to mid
        #search in left half
        if l> 0 and nums[0] <= target <= nums[l-1]:
            left = 0
            right = l - 1
            while left <= right:
                m = left + (right - left) // 2
                if nums[m] > target:
                    right = m - 1
                elif nums[m] < target:
                    left = m + 1
                else:
                    return m 
        #search in right half
        else:
            left = l
            right = len(nums)-1
            while left <= right:
                m = left + (right - left) // 2
                if nums[m] > target:
                    right = m - 1
                elif nums[m] < target:
                    left = m + 1
                else:
                    return m        
        return -1      