#BUCKET SORT: array of lists
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []
        buckets = []
        count ={}
        #set up dict
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else: 
                count[nums[i]] += 1
        
        #bucket time create, +1 extra
        for i in range(len(nums) + 1):
            buckets.append([])

        #loop over both keys and values in dict
        for key,value in count.items():
            buckets[value].append(key)
        #most frequent start from the back
        for i in range(len(buckets)-1, -1, -1):
            for num in buckets[i]:
                #keep adding until reach k most frequent
                res.append(num)
                #check if its k 
                if len(res) == k:
                    return res
 