class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_seq = 0
        num_set = set(nums)
        
        for num in nums:
            if num - 1 not in num_set:
                curr_num = num
                curr_seq = 1
                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_seq += 1
                max_seq = max(curr_seq, max_seq)
        return max_seq
                