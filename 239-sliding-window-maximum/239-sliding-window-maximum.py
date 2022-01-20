class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        
        l = r = 0
        
        q = deque() #contains index
        
        while r < len(nums):
            
            while q and nums[q[-1]] < nums[r]:
                q.pop()
            
            q.append(r)
            
            if l > q[0]:
                q.popleft()
            #so it doesnt append until min window size reached
            if (r - l + 1) >= k:
                res.append(nums[q[0]])
                l += 1
            r += 1
        return res