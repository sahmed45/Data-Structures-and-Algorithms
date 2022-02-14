class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def feasible(capacity):
            currCap = capacity
            d = 1
            i = 0
            n = len(weights) - 1
            
            while i <= n:
                if weights[i] <= currCap:
                    currCap -= weights[i]
                    i += 1
                else:
                    currCap = capacity
                    d += 1
                    if d > days:
                        return False
            return True
        
        l, r = max(weights), sum(weights)
        res = l
        while l <= r:
            mid = (l + r) // 2
            if feasible(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res