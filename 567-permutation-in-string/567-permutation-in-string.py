class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
#         if len(s1) > len(s2):
#             return False
        
#         s1freq =  [0]*26
#         s2freq =  [0]*26
        
#         for i in range(len(s1)):
#             s1freq[ord(s1[i])-ord('a')] += 1
#             s2freq[ord(s2[i])-ord('a')] += 1 
            
#         if s1freq == s2freq:
#             return True
        
#         for i in range(len(s1),len(s2)):
            
#             s2freq[ord(s2[i])-ord('a')] += 1
#             s2freq[ord(s2[i-len(s1)])-ord('a')] -= 1
            
#             if s1freq == s2freq:
#                 return True
        
#         return False


        # Check if it is even possible to have a permutation
        if len(s1) > len(s2):
            return False
    
        count = Counter(s1)
        # Set up the range for sliding window
        left, right = 0, len(s1)
        
        # Count the letters for the current sliding window
        window = Counter(s2[left:right])
        
        while right <= len(s2):
            # Found a permutation
            if count == window:
                return True
            
            # If key would become 0, delete it.
            if window[s2[left]] > 1:
                window[s2[left]] -= 1
            else:
                del window[s2[left]]
            
            # Add / Increase the next letter in the string if it exists
            if right + 1 <= len(s2):
                window[s2[right]] += 1
            
            # Move the sliding window
            left += 1
            right += 1
            
        return False