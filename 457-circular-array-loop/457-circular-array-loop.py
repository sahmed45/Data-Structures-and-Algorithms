class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:        
    	s, l = set(), len(nums)
    	for i, n in enumerate(nums):
    		if i in s: continue                 
    		d,j,last = set(),i,i
    		while n*nums[j]>0:               
    			if j in d:
    				if last!=j: return True 
    				else: break
    			d.add(j)
    			s.add(j)                     
    			j,last = (j+nums[j])%l,j
    	return False