class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        
        for index in range(len(intervals)):
            if newInterval[1] < intervals[index][0]:
                output.append(newInterval)
                return output + intervals[index:]
            elif newInterval[0] > intervals[index][1]:
                output.append(intervals[index])
            else:
                newInterval = [min(intervals[index][0],newInterval[0]),max(intervals[index][1],newInterval[1])]
        output.append(newInterval)
        
        return output