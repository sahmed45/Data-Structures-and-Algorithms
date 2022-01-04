class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSub = nums[0]
        currSub = 0
        
        for r in range(len(nums)):
            if currSub < 0:
                currSub = 0
            currSub += nums[r]
            maxSub = max(maxSub, currSub)
        return maxSub