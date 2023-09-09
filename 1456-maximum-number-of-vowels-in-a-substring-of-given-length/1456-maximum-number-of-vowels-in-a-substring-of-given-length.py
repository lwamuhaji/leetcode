class Solution:
    @staticmethod
    def count_vowels(s):
        count = 0
        for c in s:
            if c in ['a', 'e', 'i', 'o', 'u']:
                count += 1
        return count
        
    def maxVowels(self, s: str, k: int) -> int:
        count = Solution.count_vowels(s[:k])
        max_count = count
        vowel = ['a', 'e', 'i', 'o', 'u']
        for i in range(1, len(s)-k+1):
            if s[i-1] in vowel:
                count -= 1
            if s[i-1+k] in vowel:
                count += 1
            if count > max_count:
                max_count = count
        return max_count