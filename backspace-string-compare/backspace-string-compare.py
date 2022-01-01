class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        sStack =[]
        tStack =[]
        for i in range(len(s)):
            sStack.append(s[i])
            while sStack and sStack[-1] == '#':
                sStack.pop()
                if sStack:
                    sStack.pop()
        for j in range(len(t)):
            tStack.append(t[j])
            while tStack and tStack[-1] == '#':
                tStack.pop()
                if tStack:
                    tStack.pop()
        return tStack==sStack