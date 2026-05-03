#mysolution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0;
        r = len(nums)-1
        while(l<=r):
            mid = (int)(l+r)//2
            if(nums[mid]) == target:
                return mid
            #check if left half is sorted
            if nums[l] <= nums[mid]:
                #target is within the left halfs range, search
                if nums[l]<= target <=nums[mid]:
                    r = mid-1
                #target is outside the left half range, must be on right
                else:
                    l = mid + 1
            #check if right half is sorted
            else:
                #target falls within the right half range so search right
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                #target falls within left , search left 
                else:
                    r = mid -1
        return -1