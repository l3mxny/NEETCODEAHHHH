class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(2*len(nums)):
            #wraparound
            i = i % len(nums)
            result.append(nums[i])
        return result