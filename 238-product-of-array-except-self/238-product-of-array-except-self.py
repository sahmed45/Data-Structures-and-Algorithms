class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [1] * len(nums)
        prefix = 1
        postfix = 1
        length = len(nums)

        for i in range(length):
            answer[i] = prefix #start at 1
            prefix *= nums[i] #update prefix
        for i in reversed(range(length)):
            answer[i] *= postfix
            postfix *= nums[i]
            
        return answer