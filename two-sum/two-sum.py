class Solution:
    def twoSum(self, nums, target):
        length = len(nums)
        for i in range(length):
            for j in range(i+1, length):
                remainder = target - nums[i]
                if nums[j] ==remainder:
                    return [i,j]
        return None