from math import gcd

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        ab = a * b // gcd(a, b)
        bc = b * c // gcd(b, c)
        ac = a * c // gcd(a, c)
        abc = ab * c // gcd(ab, c)
        
        def uglyNumCount(k):
            return k//a + k//b + k//c - k//ab - k//ac -k//bc + k//abc
        
        left = n
        right = n * min(a,b,c)
        res = right
        
        while left <= right:
            mid = (left + right) // 2
            if uglyNumCount(mid) >= n:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
