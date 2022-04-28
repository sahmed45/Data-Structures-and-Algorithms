class Solution:
    def fib(self, n: int) -> int:
#         memo = {}
        
#         def F(i):
#             if i < 2:
#                 return i
#             if i not in memo:
#                 memo[i] = F(i - 1) + F(i - 2)
#             return memo[i]
#         return F(n)
        
        F = {}
        F[0], F[1] = 0, 1 # base cases
        for i in range(2, n + 1): # topological order
            F[i] = F[i - 1] + F[i - 2] # relation
        return F[n] # original