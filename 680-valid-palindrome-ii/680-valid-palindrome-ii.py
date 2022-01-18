class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def validSub(s,l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True
        
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return validSub(s,l+1, r) or validSub(s,l,r -1)
            l += 1
            r -= 1
        return True