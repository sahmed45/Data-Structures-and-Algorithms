class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0
        
        
        while i < len(firstList) and j < len(secondList):
            #check for overlap
            start = max(firstList[i][0],secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                res.append([start,end])
            
            #have to remove smallest end
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return res