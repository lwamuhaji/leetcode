class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = [c.lower() for c in s if c.isdigit() or c.isalpha()]
        return new_s == new_s[::-1]
        for left, right in zip(new_s, new_s[::-1]):
            if left != right:
                return False
        return True