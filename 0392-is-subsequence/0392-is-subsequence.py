class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        found = 0
        for c in s:
            while i < len(t):
                if c == t[i]:
                    i+= 1
                    found += 1
                    break
                else:
                    i += 1
        return found == len(s)