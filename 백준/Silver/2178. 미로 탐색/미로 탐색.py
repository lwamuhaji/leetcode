from collections import deque

# N, M 입력받기
N, M = map(int, input().split())
# 미로 입력받기
maze = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
for x in range(N):
    line = input()
    for y, n in enumerate(line):
        maze[x][y] = int(n)

# DFS 탐색
current = None
queue = deque([(0, 0, 1)])
visited[0][0] = True
tblr = [(-1, 0), (1, 0), (0, -1), (0, 1)]

while queue:
    current = queue.popleft()
    if current[0] == N-1 and current[1] == M-1:
        print(current[2])
        break
    
    for offset in tblr:
        x, y = current[0] + offset[0], current[1] + offset[1]
        if 0 <= x < N and 0 <= y < M and maze[x][y] and not visited[x][y]:
            queue.append((x, y, current[2] + 1))
            visited[x][y] = True