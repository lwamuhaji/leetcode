from collections import deque

def count_with_bfs(node, wires):
    count = 1
    visited = [False for _ in range(101)]
    visited[node] = True
    queue = deque([node])
    
    while queue:
        current_node = queue.popleft()
        for wire in wires:
            target_node = sum(wire) - current_node
            if (current_node == wire[0] or current_node == wire[1]) and not visited[target_node]:
                queue.append(target_node)
                count += 1
                visited[target_node] = True
    return count
            
def solution(n, wires):
    min = n
    for i in range(len(wires)):
        count1 = count_with_bfs(wires[i][0], wires[:i] + wires[i+1:])
        count2 = count_with_bfs(wires[i][1], wires[:i] + wires[i+1:])
        if min > abs(count1 - count2):
            min = abs(count1 - count2)
    return min