class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subset = [[]]
        
        for num in nums: 
            for i in range(len(subset)):
                subset.append(subset[i] + [num])
        return subset