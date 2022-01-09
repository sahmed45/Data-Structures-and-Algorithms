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
''''class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k = len(nums) - k
        def quickSelect(nums, k):

            pivot = random.choice(nums)
            if len(nums) < 2:
                return pivot
            greaterThanPivot = [x for x in nums if x > pivot]
            lessThanPivot = [x for x in nums if x <= pivot]
        
            greaterLength = len(greaterThanPivot)
            lesserLength = len(lessThanPivot)
        
            if lesserLength > k: return quickSelect(lessThanPivot, k )
            else: return quickSelect(greaterThanPivot, k - greaterLength )

        return quickSelect(nums, k)'''