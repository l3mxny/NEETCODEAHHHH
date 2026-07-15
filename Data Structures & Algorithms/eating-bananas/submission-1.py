import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        piles.sort()
        left = 1 
        right = piles[len(piles)-1]
        compare = right 
        while left <= right:
            sum = 0 
            mid = left + (right - left) // 2
            for i in range(len(piles)):
                sum += math.ceil(piles[i]/mid)
            if sum > h:
               left = mid + 1
            elif sum < h:
                compare = min(compare,mid)
                right = mid - 1
            else:
                compare = min(compare,mid)
                right = mid - 1
        return compare


        