class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) !=len(t):
            return False
        
        mapping = {}
        reverseMapping = {}
        
        for i in range(len(s)):
            if s[i] in mapping:
                if mapping[s[i]] != t[i]: return False
            elif t[i] in reverseMapping:
                if reverseMapping[t[i]] != s[i]: return False
                
            mapping[s[i]]= t[i]
            reverseMapping[t[i]]= s[i]
        return True
        
