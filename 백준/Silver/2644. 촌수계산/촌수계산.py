n = int(input())
p1, p2 = map(int, input().split())
p1 -= 1
p2 -= 1
m = int(input())

adj = [[] for _ in range(n)]
visited = [False] * n
current = None
stack = [(p1, 0)]
visited[p1] = True

for _ in range(m):
    v1, v2 = map(int, input().split())
    v1 -= 1
    v2 -= 1
    adj[v1].append(v2)
    adj[v2].append(v1)

found = False
    
while stack:
    current = stack.pop()
    if current[0] == p2:
        found = True
        print(current[1])
        break
    for p in adj[current[0]]:
        if not visited[p]:
            stack.append((p, current[1] + 1))
            visited[p] = True

if not found:
    print(-1)