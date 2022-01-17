class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        smallest_sum = math.inf
        
        nums.sort()
        
        for i in range(len(nums) -2):
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                current_sum = nums[i] + nums[r] + nums[l]
                
                if current_sum > target:
                    r -= 1
                else:
                    l += 1
                # use abs to avoid negative results
                if abs(target - current_sum) < abs(target - smallest_sum):
                    smallest_sum = current_sum
                    
        return smallest_sum