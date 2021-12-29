class Solution:
    def twoSum(self, nums, target):
        hashMap = {}
        
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashMap:
                return [hashMap[complement], i]
            hashMap[nums[i]] = i