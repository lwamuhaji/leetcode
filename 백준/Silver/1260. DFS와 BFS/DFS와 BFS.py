N, M, V = map(int, input().split())

adj_map = [[0] * (N + 1) for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    adj_map[v1][v2] = 1
    adj_map[v2][v1] = 1

stack = [V]
visited = [False] * (N + 1)
current = None
while stack:
    current = stack.pop()
    if visited[current]: continue
    visited[current] = True
    temp = []
    for idx, flag in enumerate(adj_map[current]):
        if flag and not visited[idx]:
            temp.append(idx)
    stack += temp[::-1]
    print(current, end=' ')
print()

queue = [V]
visited = [V]
current = None
while queue:
    current = queue.pop(0)
    for idx, flag in enumerate(adj_map[current]):
        if flag and idx not in visited:
            queue.append(idx)
            visited.append(idx)
    print(current, end=' ')