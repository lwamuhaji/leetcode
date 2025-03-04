from sys import stdin
input = stdin.readline
N = int(input())
nums = [int(input()) for _ in range(N)]
max_num = max(nums)
dp = [0] * (max_num + 1)
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, max_num + 1):
    v = 0
    for j in range(i-3, i):
        v += dp[j]
    dp[i] = v

for n in nums:
    print(dp[n])
    