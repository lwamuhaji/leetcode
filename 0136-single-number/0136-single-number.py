class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        number = 0
        for n in nums:
            number ^= n
        return number