class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        output = []
        l, r = 0, 0
        q = deque()
        
        while r < len(nums):
            while q and nums[q[-1]] < nums[r]:
                #pop from right to remove lowest
                q.pop()
            
            q.append(r)
            
            if l > q[0]:
                #left index beyond q index, pop from left to remove first
                q.popleft()
            
            if (r -l + 1) >= k:
                #so it doesnt append until min window size reached
                output.append(nums[q[0]])
                l += 1
            r += 1
            
        return output