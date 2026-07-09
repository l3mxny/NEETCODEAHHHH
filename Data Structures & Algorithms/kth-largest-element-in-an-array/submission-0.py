#heap?
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for n in nums:
            heapq.heappush(heap,n)
            if len(heap) > k:
                #always keep k elements size of min heap
               heapq.heappop(heap) 
        heapq.heapify(heap)
        return heap[0]
        