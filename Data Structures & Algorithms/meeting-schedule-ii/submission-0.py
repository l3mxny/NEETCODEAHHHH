"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0 
        res = 0 
        start = [x.start for x in intervals]
        end = [x.end for x in intervals]
        start.sort()
        end.sort()
        i = 0 
        j = 0 
        while i < len(start):
            if start[i] < end[j]:
                count += 1
                i += 1
            else:
                count -= 1
                j += 1
            res = max(res,count)
        return res
        