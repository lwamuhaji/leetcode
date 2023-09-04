class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maximum = n = sum(nums[:k])
        for i in range(len(nums)-k):
            n = n - nums[i] + nums[i+k]
            if maximum < n:
                maximum = n
        return maximum / k