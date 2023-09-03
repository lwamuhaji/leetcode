class Solution:
    def reverseVowels(self, s: str) -> str:
        result = ''
        vowels = [c for c in s if c in ['A', 'a', 'E', 'e', 'I', 'i','O', 'o','U', 'u']] # eo
        consonants = [c for c in s if c not in ['A', 'a', 'E', 'e', 'I', 'i','O', 'o','U', 'u']] # hll
        for c in s:
            if c in ['A', 'a', 'E', 'e', 'I', 'i','O', 'o','U', 'u']:
                result += vowels.pop()
            else:
                result += consonants.pop(0)
        return result