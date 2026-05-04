#mysolution
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l=0
        r=1
        maxProf=0;
        while r<len(prices):
            if prices[r]>prices[l]:
                if(prices[r]-prices[l] > maxProf):
                    maxProf = prices[r]-prices[l]
                r+=1
            elif prices[r]<prices[l]:
                l = r
                r+=1
            else :
                r+=1
        return maxProf