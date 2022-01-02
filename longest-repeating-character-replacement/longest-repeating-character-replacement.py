class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        repeat = 0 
        length = 0
        subMap = {}

        for right in range(len(s)):
            if s[right] not in subMap:
                subMap[s[right]] = 0
            subMap[s[right]] += 1

            repeat = max( repeat, subMap[s[right]])

            while (right - left + 1 - repeat) > k:
                subMap[s[left]] -= 1
                left += 1
            length = max(length, right - left + 1)
        return length
