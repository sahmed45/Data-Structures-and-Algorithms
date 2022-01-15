class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        res = 0
        minHeight = math.inf
        while l < r:
            minHeight = min(height[l], height[r])
            area = minHeight * (r - l)
            
            res = max(area, res)
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return res
        
        