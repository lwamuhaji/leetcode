N, M = map(int, input().split())
mat = []
visited = [[False for _ in range(M)] for _ in range(N)]

def bfs(x, y):
    if mat[x][y] == 0 or visited[x][y]:
        return -1
    
    size = 0
    queue = [(x, y)]
    visited[x][y] = True
    while queue:
        cx, cy = queue.pop(0)
        size += 1
        for dx, dy in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M and mat[nx][ny] == 1 and not visited[nx][ny]:
                queue.append((nx, ny))
                visited[nx][ny] = True
    return size
        
for _ in range(N):
    mat.append(list(map(int, input().split())))

result = [res for x in range(N) for y in range(M) if (res := bfs(x, y)) > 0]
print(len(result))
print(max(result + [0]))