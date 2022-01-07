class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        result = []
        closed = s.count(')')
        opened = 0
        
        for c in s:
            if c == ('('):
                if opened == closed: continue
                opened += 1
            elif c == (')'):
                closed -= 1
                if not opened: continue
                opened -= 1
            result.append(c)
        
        return ''.join(result)