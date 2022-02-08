"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        #error checking
        if not schedule: return []
        
        #breaking down into one list
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start,interval.end])
        #sort by starting time
        intervals.sort(key = lambda x: x[0])
        
        #loop to check for free time
        result = []
        lastEnd = intervals[0][1]
        for i in range(1, len(intervals)):
            currStart = intervals[i][0]
            if currStart > lastEnd:
                result.append(Interval(lastEnd, currStart))
            lastEnd = max(lastEnd, intervals[i][1])   
        return result