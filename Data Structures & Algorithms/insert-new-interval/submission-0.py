class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                #add new interval to front
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                #current interval comes before new interval, just add as is 
                res.append(intervals[i])
            else:
                #initially set the merge 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
        #only add new interval once we loop through all 
        res.append(newInterval)
        return res
