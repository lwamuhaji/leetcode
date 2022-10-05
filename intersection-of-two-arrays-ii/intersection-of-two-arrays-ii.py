class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d1 = dict()
        d2 = dict()
        result = []
        for n in nums1:
            d1[n] = d1.get(n, 0) + 1
        for n in nums2:
            d2[n] = d2.get(n, 0) + 1
        for n in d1:
            if n in d2:
                result += [n] * min(d1[n], d2[n])
        return result