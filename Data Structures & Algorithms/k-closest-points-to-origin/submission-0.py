class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        #move through each array in list of arrays
        for x,y in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (-dist, x,y))
            if len(heap) > k:
                #remove biggest one
                heapq.heappop(heap)
        heapq.heapify(heap)
        res = []
        while k > 0:
            #extract values from pop
            dist,x,y = (heapq.heappop(heap))
            res.append([x,y])
            k -= 1
        return res
        
            

        