from collections import deque

N, M = map(int, input().split())

m = []

for _ in range(N):
    row = input()
    row_list = []
    for c in row:
        row_list.append(int(c))
    m.append(row_list)

queue = deque([(0, 0, 1)])
visited = [[False for _ in range(M)] for _ in range(N)]
visited[0][0] = True
dist = [(0, 1), (1, 0), (-1, 0), (0, -1)]

while queue:
    x, y, cost = queue.popleft()
    if x == N-1 and y == M-1:
        print(cost)
        break
    for dx, dy in dist:
        if x+dx >= 0 and y+dy >= 0 and x+dx < N and y+dy < M:
            if m[x+dx][y+dy] == 1 and not visited[x+dx][y+dy]:
                queue.append((x+dx, y+dy, cost+1))
                visited[x+dx][y+dy] = True
    
    
