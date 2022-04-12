class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        prefix = postfix = 1
        ans = [1] * length
        #update prefix
        for i in range(length):
            ans[i] = prefix
            prefix *= nums[i]
       #for postfix, update in reverse 
        for i in range(length - 1, -1, -1):
            ans[i] *= postfix
            postfix *= nums[i]

        return ans