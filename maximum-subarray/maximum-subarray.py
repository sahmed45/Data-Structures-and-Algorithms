class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum, currSum, window = nums[0], 0, 0
        
        for i in range(len(nums)):
            if currSum <0:
                currSum =0
            currSum += nums[i]
            maxSum = max(maxSum, currSum)
        return maxSum