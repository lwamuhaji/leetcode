class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i, n in enumerate(digits[::-1]):
            n += 1
            if n == 10:
                digits[len(digits)-i-1] = 0
                if i == len(digits)-1:
                    digits.insert(0, 1)
            else:
                digits[len(digits)-i-1] = n
                break
        return digits