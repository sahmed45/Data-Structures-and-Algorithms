class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = 0
        r = len(nums) - 1
        output = []
        
        while l <= r:
            l_squared = nums[l] ** 2
            r_squared = nums[r] ** 2
            
            if l_squared > r_squared:
                output.append(l_squared)
                l += 1
            else:
                output.append(r_squared)
                r -= 1
        return output[::-1]