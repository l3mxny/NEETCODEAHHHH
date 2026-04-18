#mysolution
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ret = {}
        for n in nums:
            if n in ret:
                ret[n]+=1
            else:
                ret[n]=1
        res = sorted(ret, key=lambda x: ret[x], reverse=True)
        #sort each number by its frequency 
        ## lambda:
        #lambda x: ret[x]
        #def someFunction(x):
             #return ret[x]
        return res[:k]
        #give first k elements of loop


      
        