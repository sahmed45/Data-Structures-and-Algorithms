class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r
        
        def hours(mid):
            hours = 0
            #check total hours to eat
            for p in piles:
                hours += math.ceil(p/mid)
            return hours
        
        while l <= r:
            mid = (l + r) // 2
            
            if hours(mid) <= h:
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        return res