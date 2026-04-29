#mysolution
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ret = []
        for i in range(len(nums)):
            first = nums[i]
            if i > 0 and first == nums[i-1]:
                continue
            left = i + 1
            right = len(nums)-1
            while (left < right):
                if first + nums[left] + nums[right] == 0:
                    ret.append([first,nums[left],nums[right]])
                    left +=1
                    right -=1
                    while(nums[left] == nums[left-1] and left < right) :
                        left += 1
                    while(nums[right] == nums[right-1] and left <right):
                        right +=1 
                elif first + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    left +=1
        return ret
        
        