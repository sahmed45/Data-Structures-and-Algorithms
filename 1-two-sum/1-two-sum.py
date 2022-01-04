class Solution:
    def twoSum(self, nums, target):
        valMap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in valMap:
                return [i, valMap[complement]]
            valMap[nums[i]] = i
