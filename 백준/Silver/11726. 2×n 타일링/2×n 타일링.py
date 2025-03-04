N = int(input())
dp = [0] * (N+1)
def f(n):
    if n == 1: return 1
    if n == 2: return 2
    if dp[n]:
        return dp[n]
    else:
        dp[n] = f(n-1) + f(n-2)
        return dp[n]
print(f(N)%10007)