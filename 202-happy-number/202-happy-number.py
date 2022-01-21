class Solution:
    def isHappy(self, n: int) -> bool:
        #logn time and space
        
        #cycle if visited more than once, use set
#         visit = set()
        
#         while n not in visit:
#             visit.add(n)
#             n = self.sumOfSquares(n)
#             if n == 1:
#                 return True
#         return False

#floyd tortoise hare, logn time, 1 space

        fast = n
        slow = n
        
        while True:
            fast = self.sumOfSquares(self.sumOfSquares(fast))
            slow = self.sumOfSquares(slow)
            if fast == slow:
                break
        return slow == 1
            
        
    def sumOfSquares(self, n):
            _sum = 0
            #isolate last digit, square, then divide
            while n > 0:
                digit = n % 10
                digit = digit ** 2
                _sum += digit
                n = n // 10
            return _sum

        