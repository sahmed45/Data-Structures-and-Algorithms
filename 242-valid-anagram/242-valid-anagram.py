class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counter = {}
        
        if len(s) != len(t):
            return False
        
        for char in s:
            counter[char] = counter.get(char, 0) + 1
        for char in t:
            counter[char] = counter.get(char, 0) - 1
        
        for val in counter.values():
            if val != 0:
                return False
        return True