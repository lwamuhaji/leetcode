# parents에서 node의 부모 찾기
def get_parent(parents, node):
    # 부모가 자기 자신이면 자기 자신 반환
    if parents[node] == node:
        return node
    # 부모가 다른 노드이면 그 노드의 부모를 반환
    return get_parent(parents, parents[node])

def solution(n, costs):
    answer = 0
    costs.sort(key=lambda x: x[2])    
    parents = [_ for _ in range(n)]
    
    bridges = 0
    for cost in costs:
        # 연결하려는 두 부모의 노드가 다른 경우
        if get_parent(parents, cost[0]) != get_parent(parents, cost[1]):
            # 연결한다.
            answer += cost[2]
            
            # 
            parents[get_parent(parents, cost[0])] = cost[1]
            bridges += 1
        if bridges == n - 1:
            break
    return answer
    
    return sum(cost[2] for cost in used)