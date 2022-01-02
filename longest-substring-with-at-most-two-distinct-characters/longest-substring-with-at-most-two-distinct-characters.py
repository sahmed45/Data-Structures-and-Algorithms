class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        left = 0
        maxLength = 0
        charMap = {}
        
        for right in range(len(s)):
            rightChar = s[right]
            if rightChar not in charMap:
                charMap[rightChar] = 0
            charMap[rightChar] += 1
            
            if len(charMap) > 2:
                leftChar = s[left]
                charMap[leftChar] -= 1
                if charMap[leftChar] == 0:
                    del charMap[leftChar]
                left += 1
            maxLength = max(maxLength, right - left + 1)
        return maxLength