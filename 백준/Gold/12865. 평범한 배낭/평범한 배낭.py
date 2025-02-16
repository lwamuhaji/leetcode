N, K = map(int, input().split())

items = []
for i in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

memo = [[-1] * K for _ in range(N)]

def sol(i, w):
    if i <= 0 or w <= 0:
        return 0
    if memo[i-1][w-1] != -1:
        return memo[i-1][w-1]
    
    weight, value = items[i - 1]
    if weight <= w:
        memo[i-1][w-1] = max(sol(i-1, w), sol(i-1, w-weight) + value)
    else:
        memo[i-1][w-1] = sol(i-1, w)
    return memo[i-1][w-1]
print(sol(N, K))