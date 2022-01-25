class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        answer = 0
        left = -1
        length = len(seats)
        
        for right in range(length):
            if seats[right]:
                answer = max(answer , right if left == -1 else (right - left) // 2)
                left = right
        return max(answer, length - 1 - left)