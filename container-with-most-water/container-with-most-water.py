class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        
        l,r = 0, len(height) - 1
        while l < r:
            length = min(height[l], height[r])
            width = r - l
            area = length * width
            maxArea = max(area, maxArea)
            if height[l] < height[r]:
                l +=1
            else:
                r -= 1
        return maxArea