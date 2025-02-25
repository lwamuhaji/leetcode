from collections import deque
t = int(input())
for _ in range(t):
    n = int(input())
    positions = []
    queue = deque([0])
    visited = [False] * (n+2)
    visited[0] = True
    current = None
    for i in range(n+2):
        positions.append(tuple(map(int, input().split())))
    answer = "sad"
    while queue:
        current = queue.popleft()
        if current == n+1:
            answer = "happy"
        for i, p in enumerate(positions):
            d = abs(p[0] - positions[current][0]) + abs(p[1] - positions[current][1])
            if 0 < d <= 1000 and not visited[i]:
                queue.append(i)
                visited[i] = True
    print(answer)