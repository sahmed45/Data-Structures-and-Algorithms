class Solution:
    def findMin(self, nums: List[int]) -> int:
        N=len(nums) 
        start=0
        end=N-1
        while start<end:
            mid=(start+end)//2
			# add this line to handle duplicate
            while nums[mid]==nums[end] and mid<end:
                end-=1
            if nums[mid]>nums[end]:
                start=mid+1
            else:
                end=mid
        return nums[start]