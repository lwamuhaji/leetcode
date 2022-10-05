class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        indices = []
        for i, n in enumerate(nums):
            if n == 0:
                indices.append(i)
        for n, i in enumerate(indices):
            nums.pop(i-n)
            nums.append(0)