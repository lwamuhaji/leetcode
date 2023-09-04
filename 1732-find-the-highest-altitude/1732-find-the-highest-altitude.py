class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        now = 0
        max = 0
        for g in gain:
            now += g
            if max < now:
                max = now
        return max