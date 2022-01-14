class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        postfix = 1

        for i in range(len(nums)):
            answer[i] = prefix #start at 0
            prefix *= nums[i] #update prefix
        for i in reversed(range(len(nums))):
            answer[i] *= postfix
            postfix *= nums[i]
            
        return answer