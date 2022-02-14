class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        res = -1
        
        while l <= r:
            mid = (l + r)//2
            if arr[mid] >= arr[mid + 1] or mid == len(arr):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res