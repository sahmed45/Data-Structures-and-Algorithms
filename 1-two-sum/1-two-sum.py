class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        
        for i, n in enumerate(nums):
            diff = target - n
            
            if diff in numsMap:
                return [numsMap[diff], i]
            numsMap[n] = i
        return