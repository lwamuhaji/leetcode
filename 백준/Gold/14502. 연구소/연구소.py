from collections import deque
from itertools import combinations

r, c = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(r)]

empty = [(i, j) for i in range(r) for j in range(c) if mat[i][j] == 0]
polluted = [(i, j) for i in range(r) for j in range(c) if mat[i][j] == 2]

min_cnt = 99
for walls in combinations(empty, 3):
    for x, y in walls: mat[x][y] = 1
    queue = deque(polluted)
    visited = [[False]*c for _ in range(r)]
    cnt = 0
    while queue:
        x, y = queue.popleft()
        cnt += 1
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x+dx, y+dy
            if 0 <= nx < r and 0 <= ny < c and not visited[nx][ny] and mat[nx][ny] == 0:
                queue.append((nx,ny))
                visited[nx][ny] = True
    min_cnt = min(cnt, min_cnt)
    for x, y in walls: mat[x][y] = 0
print(len(empty) - 3 - min_cnt + len(polluted))