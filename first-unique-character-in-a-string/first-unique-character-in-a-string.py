class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = Counter(s)
        for i, c in enumerate(s):
            if hashmap[c] == 1:
                return i
        return -1