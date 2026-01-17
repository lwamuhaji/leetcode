N, M = map(int, input().split())
mat = [list(map(int, input())) for _ in range(N)]

visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True
queue = [(0, 0, 1)]

while queue:
    x, y, cost = queue.pop(0)
    if x == N-1 and y == M-1:
        print(cost)
    for dx, dy in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        cx, cy = x + dx, y + dy
        if 0 <= cx < N and 0 <= cy < M and mat[cx][cy] and not visited[cx][cy]:
            queue.append((cx, cy, cost+1))
            visited[cx][cy] = True