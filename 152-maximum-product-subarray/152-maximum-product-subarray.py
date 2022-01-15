class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        answer = max(nums)
        
        currMin, currMax = 1, 1
        
        for n in nums:
            #handle edge case
            if n == 0:
                currMin, currMax = 1, 1
            tmp = currMax * n  #tmp variable since currMax will change  
            currMax = max(n * currMax, n * currMin, n)
            currMin = min(tmp, n * currMin, n)
            answer = max(answer, currMax)
        return answer