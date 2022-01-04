class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = math.inf
        l = 0
        currSum = 0
        for r in range(len(nums)):
            currSum += nums[r]
            while currSum >= target:
                minLength = min(minLength, r - l + 1 )
                currSum -= nums[l]
                l += 1
            
            
        if minLength == math.inf: return 0    
        return minLength
            
