class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        short = min(len(word1), len(word2))
        for i in range(short):
            result.append(word1[i] + word2[i])
        if len(word1) > len(word2):
            result += word1[short:]
        else:
            result += word2[short:]
        return ''.join(result)