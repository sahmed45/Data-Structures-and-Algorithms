class Solution:
    def climbStairs(self, n: int) -> int:
        # imagine a decision tree
        #bottom up DP, start at base case
        one, two = 1, 1
        
        for i in range(n - 1):
            tmp = one
            one = one + two
            two = tmp
        return one
        