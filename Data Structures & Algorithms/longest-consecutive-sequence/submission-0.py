#mysolution
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        ret = 0
        
        for i in s:
            if i-1 not in s:
                length=1
                start = i
                while i+1 in s:
                    length += 1
                    i+=1
                ret = max(ret,length)
        return ret