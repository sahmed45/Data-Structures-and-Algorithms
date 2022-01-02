class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        windowStart = 0
        charMap = {}
        maxLength = 0
        
        for windowEnd in range(len(s)):
            rightChar = s[windowEnd]
            if rightChar not in charMap:
                charMap[rightChar] = 0
            charMap[rightChar] += 1
            
            while len(charMap) > k:
                leftChar = s[windowStart]
                charMap[leftChar] -= 1
                if charMap[leftChar] == 0:
                    del charMap[leftChar]
                windowStart += 1
            maxLength = max(maxLength, windowEnd- windowStart +1)
        return maxLength
            