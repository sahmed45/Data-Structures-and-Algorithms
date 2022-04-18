class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        water = 0
        l, r = 0 , len(height) - 1
        max_left = height[l]
        max_right = height[r]
        while l < r:
            if height[l] < height[r]:
                l += 1
                max_left = max(max_left, height[l])
                curr_height = max_left - height[l]
            else:
                r -= 1
                max_right = max(max_right, height[r])
                curr_height = max_right - height[r]
            if curr_height > 0:
                water += curr_height
            
        return water
                