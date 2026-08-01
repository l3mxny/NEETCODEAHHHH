"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    #interval object, use .start .end
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if len(intervals) <= 1:
            return True
        intervals.sort(key = lambda x:x.start)
        endNode = intervals[0].end

        for i in range(1,len(intervals)):
            #overlap
            if intervals[i].start < endNode:
                return False
            else:
                endNode = max(intervals[i].end, endNode)
        return True
