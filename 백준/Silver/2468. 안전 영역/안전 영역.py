N = int(input())
mat = [list(map(int,input().split())) for _ in range(N)]
offsets = [(1, 0), (-1, 0), (0, 1), (0, -1)]
answer = 1
for rain in range(1, 100):
    cnt = 0
    visited = [[False] * N for _ in range(N)]
    
    for i in range(N*N):
        visited[i//N][i%N] = True if mat[i//N][i%N] <= rain else False
        
    for i in range(N*N):
        x, y = i//N, i%N
        if visited[x][y]: continue
        cnt += 1
        stack = [(x, y)]
        
        while stack:
            cx, cy = stack.pop()
            for dx, dy in offsets:
                nx, ny = cx+dx, cy+dy
                if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                    visited[nx][ny] = True
                    stack.append((nx, ny))
    
    answer = max(answer, cnt)
print(answer)