class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = -stones[i]
        heapq.heapify(stones)
        while len(stones) > 1:
            a1 = -(heapq.heappop(stones))
            a2 = -(heapq.heappop(stones))
            if a1 == a2:
                continue
            else:
                a3 = a2-a1
                heapq.heappush(stones, a3)
        if len(stones) == 0:
            return 0 
        return -stones[0]
                

        