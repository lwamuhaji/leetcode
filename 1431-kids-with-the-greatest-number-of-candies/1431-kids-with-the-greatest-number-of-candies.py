class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_num = max(candies)
        minimum = max_num - extraCandies
        return [n>=minimum for n in candies]