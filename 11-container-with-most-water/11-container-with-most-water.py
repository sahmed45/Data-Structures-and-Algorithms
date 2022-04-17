class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        max_area = 0
        
        while l < r:
            width = r - l
            min_height = min(height[l], height[r])
            curr_area = width * min_height
            max_area = max(curr_area, max_area)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_area