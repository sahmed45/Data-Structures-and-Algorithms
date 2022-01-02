class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        maxSub = 0
        subMap = {}

        for right in range(len(s)):
            rightChar = s[right]
            if rightChar not in subMap:
                subMap[rightChar] = 0
            subMap[rightChar] += 1

            while subMap[rightChar] >1:
                leftChar = s[left]
                subMap[leftChar] -= 1
                if subMap[leftChar]== 0:
                    del subMap[leftChar] 
                left += 1
            maxSub = max(maxSub, right - left + 1)

        return maxSub       