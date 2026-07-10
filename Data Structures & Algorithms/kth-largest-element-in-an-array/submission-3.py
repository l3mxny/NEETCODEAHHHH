#quick select: gives k without sorting
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        target = len(nums)-k
        def quickselect(left,right):
            pivot = nums[right] 
            bound = left 
            for current in range(left,right):
                if nums[current] <= pivot:
                    temp = nums[bound]
                    nums[bound] = nums[current]
                    nums[current] = temp
                    bound += 1
            temp = nums[bound]
            nums[bound] = nums[right]
            nums[right] = temp

            if bound > target:
                return quickselect(left, bound - 1)
            elif bound < target:
                return quickselect(bound + 1, right)
            else:
                return nums[bound]

        return quickselect(0, len(nums) - 1)
            
        