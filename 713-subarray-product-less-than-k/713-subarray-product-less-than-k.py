class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k <= 1:
            return 0
        res = 0
        prod = 1
        l = 0
        
        for r, val in enumerate(nums):
            prod *= val
            
            while prod >= k:
                prod /= nums[l]
                l += 1
            res += (r - l + 1)
        return res
        