class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minLength = math.inf
        windowStart = 0
        currSum = 0 
        for i in range(len(nums)):
            currSum += nums[i]
            while currSum >= target:
                minLength = min(minLength, i - windowStart + 1)
                currSum -= nums[windowStart]
                windowStart += 1
        if minLength == math.inf:
            return 0
        return minLength