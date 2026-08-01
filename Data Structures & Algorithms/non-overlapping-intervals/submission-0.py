class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key =  lambda x:x[0])
        count = 0 
        endNode = intervals[0][1]
        #start at one so no compare same interval
        for i in range(1,len(intervals)):
            if intervals[i][0] < endNode:
                #overlap
                count += 1
                endNode = min(intervals[i][1], endNode)
            else:
                #no overlap, move end node
                endNode = intervals[i][1]
        return count

        