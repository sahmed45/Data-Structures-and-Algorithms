class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0 , len(height) - 1
        answer = 0
        maxLeft = height[l]
        maxRight = height[r]
        
        while l < r:

            if maxLeft < maxRight:
                currHeight = maxLeft - height[l]
                l += 1
                maxLeft = max(maxLeft, height[l])
            else:
                currHeight = maxRight - height[r]
                r -= 1
                maxRight = max(maxRight, height[r])
                
            if currHeight > 0:
                answer += currHeight
        return answer