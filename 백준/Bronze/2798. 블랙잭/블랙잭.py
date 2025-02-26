from itertools import combinations

N, M = map(int, input().split())
NUMS = list(map(int, input().split()))
print(M-min(filter(lambda x: x>=0, map(lambda x: M-sum(x),combinations(NUMS, 3)))))