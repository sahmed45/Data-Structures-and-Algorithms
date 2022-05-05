class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0 , len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            #left sorted
            if nums[mid] >= nums[l]:
                #the only numbers less than left must be in right side
                if target > nums[mid] or target < nums[l]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                #the only numbers greater than right must be in left side
                if target < nums[mid] or target > nums[r]:
                    r = mid - 1
                else:
                    l = mid + 1
        return -1
                    