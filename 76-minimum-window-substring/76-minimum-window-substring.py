class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""
        
        count_t, window = {}, {}
        
        for c in t:
            count_t[c] = count_t.get(c, 0) + 1
        
        have, need = 0, len(count_t)
        res = [-1,-1]
        l = 0
        length = float("infinity")
        
        for r in range(len(s)):
            c = s[r]
            window[c] = window.get(c, 0) + 1
            if c in count_t and window[c] == count_t[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < length:
                    res = [l,r]
                    length = r - l + 1
                
                window[s[l]] -= 1
                if s[l] in count_t and window[s[l]] < count_t[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        
        return s[l:r+1] if length != float("infinity") else ""