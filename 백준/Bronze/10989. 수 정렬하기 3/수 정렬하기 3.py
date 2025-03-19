from sys import stdin
input = stdin.readline
N = int(input())
nums = [0] * 10001
for i in range(N):
    nums[int(input())] += 1
for i in range(1, 10001):
    for _ in range(nums[i]):
        print(i)
