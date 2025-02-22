from collections import deque

N, K = int(input()), int(input())
adj = [[] for _ in range(N)]

for _ in range(K):
    v1, v2 = map(int, input().split())
    adj[v1-1].append(v2-1)
    adj[v2-1].append(v1-1)

current = None
visited = [False] * N
queue = deque([0])
visited[0] = True
count = 0

while queue:
    current = queue.popleft()
    count += 1
    for node in adj[current]:
        if not visited[node]:
            queue.append(node)
            visited[node] = True

print(count-1)