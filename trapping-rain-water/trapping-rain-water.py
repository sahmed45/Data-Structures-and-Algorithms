class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return 0
        totalWater = 0
        l = 0
        r = len(height) - 1
        maxLeft = height[l]
        maxRight = height[r]
        while l < r:
            if maxLeft < maxRight:
                currentWater = maxLeft - height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            else: 
                currentWater = maxRight - height[r]
                r -=1
                maxRight = max(maxRight,height[r])
                
            if currentWater >= 0:
                totalWater += currentWater
        return totalWater
