class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_neg = [-n for n in nums]
        heapq.heapify(nums_neg)
        
        for _ in range(k-1):
            heapq.heappop(nums_neg)
        return -heapq.heappop(nums_neg)