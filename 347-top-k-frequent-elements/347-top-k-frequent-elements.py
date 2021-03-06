class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        #different list for each count
        freq = [ [] for i in range(len(nums) + 1)]
        
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        #append numbers to count index
        for num, c in count.items():
            freq[c].append(num)
        
        res = []
        #iterate in reverse, highest frequency is at end
        for i in range(len(freq) -1, -1, -1):
        #append the number from the frequency to result until done k times
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
            