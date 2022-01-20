class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        l = r = 0
        
        q = deque() #contains index
        
        while r < len(nums):
            #pop from right to remove lowest
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            #left index beyond q index, pop from left to remove first
            if l > q[0]:    
                q.popleft()
            #so it doesnt append until min window size reached
            if (r - l + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res