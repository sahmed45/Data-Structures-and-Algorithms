class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickSelect(nums, k):   
            pivot = random.choice(nums)
            greaterThanPivot = [x for x in nums if x > pivot]
            equalToPivot = [x for x in nums if x == pivot]
            lessThanPivot = [x for x in nums if x < pivot]
        
            greaterLength = len(greaterThanPivot)
            equalLength = len(equalToPivot)
        
            if k <= greaterLength:
                return quickSelect(greaterThanPivot, k)
            elif k > greaterLength + equalLength:
                return quickSelect(lessThanPivot, k - greaterLength - equalLength)
            else:
                return equalToPivot[0]
        return quickSelect(nums, k)