def solution(n, edge):
    cost = [0 for _ in range(n+1)]
    visited = [False for _ in range(n+1)]
    queue = [1]
    visited[1] = True

    adj = {}
    for i in range(1, n + 1):
        adj[i] = set()
    for e in edge:
        adj[e[0]].add(e[1])
        adj[e[1]].add(e[0])

    while queue:
        current = queue.pop(0)
        for next_node in adj[current]:
            if not visited[next_node]:
                queue.append(next_node)
                visited[next_node] = True
                cost[next_node] = cost[current] + 1
        
    return cost.count(max(cost))