class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        res = 0
        while l <= r:
            mid = (l+r) // 2
            if ord(letters[mid]) > ord(target):
                res = mid
                r = mid -1
            else:
                l = mid + 1
        return letters[res]