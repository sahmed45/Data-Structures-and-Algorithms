class Solution:
    def fib(self, n: int) -> int:
        memo = {}
        
        def F(i):
            if i < 2:
                return i
            if i not in memo:
                memo[i] = F(i - 1) + F(i - 2)
            return memo[i]
        return F(n)
        