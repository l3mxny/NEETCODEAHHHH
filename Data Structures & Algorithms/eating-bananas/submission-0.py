#mysolution
import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #min speed
        minSpeed = 1
        #max speed
        maxSpeed = max(piles)
        #range of speed
        while minSpeed <= maxSpeed:
            #speed
            mid = int((minSpeed + maxSpeed)/2)
            hours = 0
            #each bannana in current pile
            for bannana in piles: 
                hours += math.ceil(bannana / mid)
            #can go even slower find mininum speed
            if hours <= h:
                maxSpeed = mid -1
            elif hours > h:
                minSpeed = mid + 1
        return minSpeed