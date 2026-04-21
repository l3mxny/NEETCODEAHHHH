class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left=[]
        right=[]
        result=[]
        left= [1]
        right = [1]
        for i in range(1,len(nums)):
            left.append(left[i-1] * nums[i-1])
        for i in range(len(nums)-2,-1,-1):
            right.insert(0,right[0]*nums[i+1])
        
        for i in range(0,len(nums)):
            result.append(left[i]*right[i])
        return result

        