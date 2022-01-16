class Solution:
    def fib(self, n: int) -> int:
#         if n == 0: return 0
#         if n == 1: return 1
        
#         return self.fib(n - 1) + self.fib(n - 2)

        if n <= 1:
            return n
        
        #think about fib 2 = fib 1 + fib 0, aka 1 + 0
        prev1 = 1
        prev2 = 0
        
        for i in range(2, n + 1):
            tmp = prev1
            prev1 = prev1 + prev2
            prev2 = tmp
        return prev1
            