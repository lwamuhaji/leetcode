N = int(input())
mat = [list(input()) for _ in range(N)]
visited = [[False for _ in range(N)] for _ in range(N)]

def bfs(x, y, flag=False):
    if visited[y][x]:
        return False
    queue = [(y, x)]
    color = mat[y][x]
    visited[y][x] = True
    while queue:
        cy, cx = queue.pop(0)
        for dy, dx in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            ny, nx = cy + dy, cx + dx
            if 0 <= nx < N and 0 <= ny < N and (color == mat[ny][nx] or (flag and color in ['R', 'G'] and mat[ny][nx] in ['R', 'G'])) and not visited[ny][nx]:
                queue.append((ny, nx))
                visited[ny][nx] = True
    return True

print(len([0 for x in range(N) for y in range(N) if bfs(x, y)]), end=" ")
visited = [[False for _ in range(N)] for _ in range(N)]
print(len([0 for x in range(N) for y in range(N) if bfs(x, y, flag=True)]))