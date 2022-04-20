class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
#         if len(s1) > len(s2):
#             return False
        
#         s1_freq = s2_freq = [0] * 26
        
#         for i in range(len(s1)):
#             s1_freq[ord(s1[i]) - ord('a')] += 1
#             s2_freq[ord(s2[i]) - ord('a')] += 1
        
#         if s1_freq == s2_freq: return True
        
#         for i in range(len(s1), len(s2)):
#             s2_freq[ord(s2[i]) - ord('a')] += 1
#             s2_freq[ord(s2[i]) - len(s1) - ord('a')] -= 1
            
#             if s1_freq == s2_freq: return True
            
#         return False
         if len(s1) > len(s2):
             return False
        
         s1freq =  [0]*26
         s2freq =  [0]*26
        
         for i in range(len(s1)):
             s1freq[ord(s1[i])-ord('a')] += 1
             s2freq[ord(s2[i])-ord('a')] += 1 
            
         if s1freq == s2freq:
             return True
        
         for i in range(len(s1),len(s2)):
            
             s2freq[ord(s2[i])-ord('a')] += 1
             s2freq[ord(s2[i-len(s1)])-ord('a')] -= 1
            
             if s1freq == s2freq:
                 return True
        
         return False