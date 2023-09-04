class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        intersection = set(nums1) & set(nums2)
        return [list(set(nums1) - intersection), list(set(nums2) - intersection)]