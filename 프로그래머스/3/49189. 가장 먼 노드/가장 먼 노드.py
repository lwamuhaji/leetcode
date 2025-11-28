import heapq

def solution(n, edge):
    dist = [float("inf") for _ in range(n+1)] # 정점 사이의 거리
    dist[1] = 0 # 자기 자신은 0
    visited = [False for _ in range(n+1)] # 방문 리스트
    queue = [(0, 1)] # 첫 방문 넣어놓기 (cost, 노드번호)
    visited[1] = True # 방문함

    # 인접리스트 만들기
    adj = {}
    for i in range(1, n + 1):
        adj[i] = set()
    for e in edge:
        adj[e[0]].add(e[1])
        adj[e[1]].add(e[0])

    while queue:
        cost, current = heapq.heappop(queue)
        visited[current] = True
        
        if(cost > dist[current]): continue # 계산할 필요 없음
        
        # 더 작은 값이 나오면 dist 갱신
        for nextNode in adj[current]:
            if dist[nextNode] > cost + 1:
                dist[nextNode] = cost + 1
                heapq.heappush(queue, (dist[nextNode], nextNode))
    
    print(dist)
        
    return dist[1:].count(max(dist[1:]))


