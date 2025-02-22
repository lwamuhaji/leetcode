N = int(input())
mat = [[0] * N for _ in range(N)]

for row in range(N):
    line = input()
    for col, n in enumerate(line):
        mat[row][col] = int(n)

visited = [[False] * N for _ in range(N)]
tdlr = [(-1, 0), (1, 0), (0, -1), (0, 1)]    
    
def dfs(start):
    if visited[start[0]][start[1]] or not mat[start[0]][start[1]]:
        return -1
    
    stack = [start]
    visited[start[0]][start[1]] = True
    count = 0
    while stack:
        current = stack.pop()
        count += 1
        for offset in tdlr:
            r, c = current[0] + offset[0], current[1] + offset[1]
            if 0 <= r < N and 0 <= c < N and mat[r][c] and not visited[r][c]:
                stack.append((r, c))
                visited[r][c] = True
    return count

answer = []
for r in range(N):
    for c in range(N):
        count = dfs((r, c))
        if count > 0:
            answer.append(count)
answer.sort()
print(len(answer))
for n in answer:
    print(n)