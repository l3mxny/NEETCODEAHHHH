#mysolution
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0 
        r = len(numbers)-1
        result = []
        while l < r:
            sum = numbers[l] + numbers[r]
            if sum > target:
                r-=1
            elif sum < target:
                l+=1
            else:
                result.append(l+1)
                result.append(r+1)
                return result