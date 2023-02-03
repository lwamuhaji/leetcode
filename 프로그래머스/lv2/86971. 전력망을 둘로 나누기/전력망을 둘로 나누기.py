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
    # 개수 차이의 최솟값. 초기값은 될 수 있는 가장 큰 수 n 으로 지정
    min = n
    
    # 모든 간선을 돌면서 하나하나 끊어본다.
    for i in range(len(wires)):
        # 끊긴 트리를 정의함
        divided_trees = wires[:i] + wires[i+1:]
        
        # 끊겨서 만들어진 두 트리의 노드 개수를 각각 카운트
        count1 = count_with_bfs(wires[i][0], divided_trees)
        count2 = count_with_bfs(wires[i][1], divided_trees)
        
        # 노드 개수의 차이를 구한다.
        diff = abs(count1 - count2)
        
        # min이 minimum이 아니면 minimum 값으로 바꿈
        if min > diff:
            min = diff
    return min


def solution(n, wires):
    ans = n
    for sub in (wires[i+1:] + wires[:i] for i in range(len(wires))):
        s = set(sub[0])
        [s.update(v) for _ in sub for v in sub if set(v) & s]
        ans = min(ans, abs(2 * len(s) - n))
    return ans