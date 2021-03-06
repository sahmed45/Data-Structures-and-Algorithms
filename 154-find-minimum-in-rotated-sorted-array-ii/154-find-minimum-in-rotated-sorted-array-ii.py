class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) -1
        
        while l < r:
            mid = (l + r) // 2
            
			# add this line to handle duplicate
            while nums[mid] == nums[r] and mid < r:
                r -= 1
            
            if nums[mid] > nums[r]:
                l = mid + 1
            
            else:
                r = mid
                            
        return nums[l]
