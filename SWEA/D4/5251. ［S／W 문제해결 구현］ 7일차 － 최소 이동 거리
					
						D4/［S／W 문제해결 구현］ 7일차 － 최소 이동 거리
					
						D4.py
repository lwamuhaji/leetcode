import heapq
from collections import defaultdict

def solution():
    graph = defaultdict(list)
    N, E = map(int, input().split())
    dist = [float('inf')] * (N+1)
    dist[0] = 0
    for _ in range(E):
        s, e, w = map(int, input().split())
        graph[s].append((e, w))

    heap = [(0, 0)]
    seen = [False] * (N+1)
    while heap:
        _, current = heapq.heappop(heap)

        if seen[current]:
            continue
        seen[current] = True

        for b, w in graph[current]:
            dist[b] = min(dist[b], dist[current] + w)
            heapq.heappush(heap, (dist[b], b))

    return dist[N]

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    print(f"#{test_case} {solution()}")