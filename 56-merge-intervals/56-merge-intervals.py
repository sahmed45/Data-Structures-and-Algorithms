class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = [intervals[0]]
        
        for interval in intervals[1:]:
            if interval[0] > output[-1][1]:
                output.append(interval)
            else:
                output[-1][1] = max(output[-1][1], interval[1])
        return output