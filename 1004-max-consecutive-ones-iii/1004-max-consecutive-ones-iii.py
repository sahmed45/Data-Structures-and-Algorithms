class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        l, maxLength, currLength = 0,0,0
        
        for r in range(len(nums)):
            if nums[r] == 1:
                currLength += 1
            
            if r - l + 1 - currLength > k:
                if nums[l] == 1:
                    currLength -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
        return maxLength