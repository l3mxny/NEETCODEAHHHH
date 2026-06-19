class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        nums.sort()
        slow = 0
        fast = 1
        while fast < len(nums):
            while fast < len(nums) and nums[slow] == nums[fast]:
                fast += 1
            if fast < len(nums):
                slow += 1
                nums[slow] = nums[fast]
                fast += 1
        return slow + 1