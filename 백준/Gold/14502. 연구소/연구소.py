from collections import deque
from itertools import combinations

r, c = map(int, input().split())
mat = []
for _ in range(r):
    mat.append(list(map(int, input().split())))

# 비어있는 곳, 오염된 곳 리스트
empty, polluted = [], []
for x in range(r):
    for y in range(c):
        if mat[x][y] == 0:
            empty.append((x, y))
        if mat[x][y] == 2:
            polluted.append((x, y))
combs = combinations(empty, 3)
min_cnt = 999999
for ((x1, y1), (x2, y2), (x3, y3)) in combs:
    mat[x1][y1], mat[x2][y2], mat[x3][y3] = 1, 1, 1
    current = None
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
    min_cnt = cnt if cnt < min_cnt else min_cnt
    mat[x1][y1], mat[x2][y2], mat[x3][y3] = 0, 0, 0
print(len(empty) - 3 - min_cnt + len(polluted))