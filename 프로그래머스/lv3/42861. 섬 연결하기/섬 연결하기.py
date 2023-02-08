from collections import deque


# 트리를 node1부터 DFS로 순회하며 node1과 node2가 연결되어 있는지 탐색
def is_connected_with(node1, node2, edges):
    visited = [False for _ in range(100)]
    queue = deque([node1])
    while queue:
        current_node = queue.popleft()
        visited[current_node] = True
        if current_node == node2:
            return True
        for edge in edges:
            if edge[0] == current_node and not visited[edge[1]]:
                queue.append(edge[1])
            if edge[1] == current_node and not visited[edge[0]]:
                queue.append(edge[0])
    return False

def solution(n, costs: list):
    costs.sort(key=lambda x: x[2])
    used = []

    for cost in costs:
        if not is_connected_with(cost[0], cost[1], used):
            used.append(cost)
    
    return sum(cost[2] for cost in used)