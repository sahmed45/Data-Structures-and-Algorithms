class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        mapping = {}
        used = set()
        
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            s_char = s[i]
            t_char = t[i]
            if s_char in mapping:
                if mapping[s_char] != t_char:
                    return False
            else:
                if t_char in used:
                    return False
                mapping[s_char] = t_char
                used.add(t_char)
        return True