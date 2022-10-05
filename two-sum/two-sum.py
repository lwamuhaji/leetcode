class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            try:
                return [i, nums.index(target - n, i+1)]
            except:
                ...