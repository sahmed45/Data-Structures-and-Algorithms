class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        output = []
        
        for idx in range(len(intervals)):  
            if intervals[idx][0] > newInterval[1]:
                output.append(newInterval)
                return output + intervals[idx:]
            elif newInterval[0] > intervals[idx][1]:
                output.append(intervals[idx])       
            else:
                newInterval = [min(intervals[idx][0],newInterval[0]), max(intervals[idx][1], newInterval[1])]
        output.append(newInterval) 
        
        return output