def solution(m, n, puddles):
    grid = [[0 for _ in range(n+1)] for _ in range(m+1)]
    grid[1][1] = 1
    for x, y in puddles:
        grid[x][y] = -1
    for x in range(1, m+1):
        for y in range(1, n+1):
            if grid[x][y] == -1:
                continue
            grid[x][y] += max(grid[x-1][y], 0) + max(grid[x][y-1], 0)
    return grid[x][y] % 1000000007