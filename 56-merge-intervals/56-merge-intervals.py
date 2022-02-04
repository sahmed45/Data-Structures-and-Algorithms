class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda i: i[0])
        output = []
        
        for start, end in intervals:
            #if no interval, ie start > end, or if no output yet
            if not output or start > output[-1][1]:
                output.append([start,end])
            else:
                output[-1][1] = max(output[-1][1], end)
        return output