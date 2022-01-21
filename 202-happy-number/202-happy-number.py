class Solution:
    def isHappy(self, n: int) -> bool:
        #cycle if visited more than once, use set
        visit = set()
        
        while n not in visit:
            visit.add(n)
            n = self.sumOfSquares(n)
            if n == 1:
                return True
        return False    
        
    def sumOfSquares(self, n):
            _sum = 0
            
            while n > 0:
                digit = n % 10
                digit = digit ** 2
                _sum += digit
                n = n // 10
            return _sum