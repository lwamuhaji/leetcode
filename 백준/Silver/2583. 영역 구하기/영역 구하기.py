M, N, K = map(int, input().split())
mat = [[True for _ in range(N)] for _ in range(M)]
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().split())
    for row in mat[y1:y2]:
        row[x1:x2] = [False] * (x2-x1)

visited = [[False for _ in range(N)] for _ in range(M)]

def bfs(x, y):
    if mat[y][x] == False or visited[y][x]:
        return -1
    size = 0
    queue = [(y, x)]
    visited[y][x] = True
    while queue:
        cy, cx = queue.pop(0)
        size += 1
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= nx < N and 0 <= ny < M and mat[ny][nx] == True and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
    return size

result = [res for x in range(N) for y in range(M) if (res := bfs(x, y)) > 0]
print(len(result))
print(*sorted(result))