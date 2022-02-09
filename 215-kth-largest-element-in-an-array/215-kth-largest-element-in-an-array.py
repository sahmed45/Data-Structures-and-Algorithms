class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #return last element, nlargest creates an array in descending order
        #last element would be smallest in that array
        return heapq.nlargest(k, nums)[-1]