class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        
        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            l, r = idx + 1, len(nums) - 1
            
            while l < r:
                curr_sum = val + nums[l] + nums[r]
                if curr_sum > 0:
                    r -= 1
                elif curr_sum < 0:
                    l += 1
                else:
                    res.append([val , nums[l] , nums[r]])
                    l += 1
                    
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res