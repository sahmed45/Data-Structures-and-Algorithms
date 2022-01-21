class Solution:
    def brightestPosition(self, lights: List[List[int]]) -> int:
        a = []
        for x, y in lights:
            a.append((x - y, 1))
            a.append((x + y + 1, -1))
        a = sorted(a)
        count = 1
        m = 1
        mp = a[0][0]
        for i in range(1, len(a)):
            count += a[i][1]
            if count > m:
                m = count
                mp = a[i][0] if a[i][1] == 1 else a[i][0] - 1
        if count > m:
            return a[-1][0] if a[-1][1] == 1 else a[-1][0] - 1
        return mp
# like this, add events to add 1 to a running total and subtract 1 from the total
# so like if you have a lamp [3, 5], then you would add to your events (3, 1) and (6, -1)
# this means that at timestamp 3, you add one, and at timestamp 6, you subtract one
# then just sort and sweep