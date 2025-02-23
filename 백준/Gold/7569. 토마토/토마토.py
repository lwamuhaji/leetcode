from collections import deque

X, Y, Z = map(int, input().split())

mat = [[[0] * X for _ in range(Y)] for _ in range(Z)]
queue = deque([])
visited = [[[-1] * X for _ in range(Y)] for _ in range(Z)]
current = None
offsets = [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]

for z in range(Z):
    for y in range(Y):
        line = map(int,input().split())
        for x, n in enumerate(line):
            mat[z][y][x] = n
            if n == 1:
                queue.append((x, y, z))
                visited[z][y][x] = 0

while queue:
    x, y, z = queue.popleft()
    for dx, dy, dz in offsets:
        nx, ny, nz = x+dx, y+dy, z+dz
        if 0 <= nx < X and 0 <= ny < Y and 0 <= nz < Z and visited[nz][ny][nx] == -1 and mat[nz][ny][nx] == 0:
            queue.append((nx,ny,nz))
            visited[nz][ny][nx] = visited[z][y][x] + 1

maximum = 0
answer = None
for z in range(Z):
    for y in range(Y):
        for x in range(X):
            maximum = visited[z][y][x] if visited[z][y][x] > maximum else maximum
            if mat[z][y][x] == 0 and visited[z][y][x] == -1:
                answer = -1

print(answer) if answer == -1 else print(maximum)