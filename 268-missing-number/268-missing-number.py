class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        i = 0
        n = len(nums)
        
        while i < n:
            j = nums[i]
            #check if range, check if number at index equals index, if not, swap
            if nums[i] < n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i:
                return i
            
        return len(nums)