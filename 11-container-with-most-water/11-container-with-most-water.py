class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height) -1
        max_water = 0
        while l < r:
            width = r - l
            length = min(height[l],height[r])
            max_water = max(max_water, width * length)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return max_water