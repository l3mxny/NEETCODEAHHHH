class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        res = []
        sum = 0 
        l = 0 
        r = len(numbers)-1
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum < target: 
                l += 1
            elif sum > target:
                r -= 1
            else:
                res.append(l + 1)
                res.append(r + 1) 
                return res

         