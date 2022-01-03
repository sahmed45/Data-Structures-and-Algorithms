class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        
        for num in nums:
            if num in count:
                count[num] +=1
                if count[num] > 1:
                    return True
            else:
                count[num] = 1
        return False