class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        if '' in strs:
            return ''
        for i, c in enumerate(strs[0]):
            for s in strs:
                if i >= len(s):
                    return s[:i]
                if s[i] != c:
                    return s[:i]
        return strs[0][:i+1]