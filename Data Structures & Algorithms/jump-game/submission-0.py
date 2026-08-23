class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goalPost = len(nums)-1
        for i in range(len(nums)-2, -1, -1):
            if i + nums[i] >= goalPost:
                goalPost = i 
        if goalPost == 0:
            return True
        else:
            return False


        