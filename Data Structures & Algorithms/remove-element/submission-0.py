class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #remove array in place 
        #one pointer scans every element, other tracks where next keps element shoudl be placed 
        l = 0 
        r = 0 
        for r in range(len(nums)):
            if nums[r] != val: 
                nums[l] = nums[r]
                l += 1 
        return l