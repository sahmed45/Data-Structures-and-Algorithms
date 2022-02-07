class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals: return 0
        
        start = sorted([i[0] for i in intervals])
        end = sorted([i[1] for i in intervals])
        s, e = 0, 0
        res, count = 0, 0
        
        while s < len(intervals):
            #if meeting starts before last one ends
            if start[s] <  end[e]:
                s += 1
                count += 1
            #if meeting ends before next start
            else:
                e += 1
                count -= 1
            res = max(count, res)
        return res