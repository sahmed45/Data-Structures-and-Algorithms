class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            j = nums[i]
            if nums[i] < n and j != i:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
        return len(nums)