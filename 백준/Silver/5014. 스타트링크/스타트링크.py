from collections import deque

F, S, G, U, D = map(int, input().split())

visited = [-1] * (F+1)
current = None
queue = deque([S])
visited[S] = 0
offsets = [U, -D]

found = False

while queue:
    current = queue.popleft()
    if current == G:
        print(visited[G])
        found = True
        break
    for offset in offsets:
        next = current + offset
        if 1 <= next <= F and visited[next] == -1:
            queue.append(next)
            visited[next] = visited[current] + 1

if not found:
    print("use the stairs")