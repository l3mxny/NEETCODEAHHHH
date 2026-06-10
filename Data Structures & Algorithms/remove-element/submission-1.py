class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #remove array in place 
        #one pointer scans every element, other tracks where next keps element shoudl be placed 
        l = 0 
        for i in range(len(nums)):
            if nums[i] != val: 
                nums[l] = nums[i]
                l += 1 
        return l