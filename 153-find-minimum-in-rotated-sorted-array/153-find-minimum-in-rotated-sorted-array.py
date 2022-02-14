class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]
        #choose last as pivot, rotated means first element will be greater than last
        pivot = nums[r]
        while l <= r:
            mid = (l + r) //2
            if nums[mid] <= pivot:
                res = nums[mid]
                r = mid - 1
            else:
                l = mid + 1
        return res