class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i, n in enumerate(nums):
        #enumerate give you both index and value 
            complement = target - n
            if complement in hashmap:
                return [hashmap[complement], i]
            #if not in hashmap, add it to the hashmap
            hashmap[n] = i
        return []
        