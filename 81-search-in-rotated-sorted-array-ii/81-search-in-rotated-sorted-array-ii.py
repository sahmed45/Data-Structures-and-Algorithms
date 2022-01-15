class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if target == nums[mid]: 
                return True
            
            # left sorted
            while nums[l]==nums[mid] and l < mid:
                l += 1
            if nums[mid] >= nums[l]:
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            #right sorted
            else:
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return False
            