class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        maxSum = nums[0]
        currSum = 0
        for r in range(len(nums)):
            if currSum < 0:
                currSum = 0       
            currSum += nums[r]
            maxSum = max(currSum, maxSum)
        return maxSum
