from collections import defaultdict, deque

def BFS(n, startNode, arr, check):
    cnt = 1
    que = deque([startNode])
    visited = [True for _ in range(n+1)]
    visited[startNode] = False

    while que:
        node = que.popleft()
        for target in arr[node]:
            if check[node][target] and check[target][node] and visited[target]:
                visited[target] = False
                que.append(target)
                cnt += 1

    return cnt

def solution(n, wires):
    answer = n
    arr = defaultdict(list)
    check = [[False for _ in range(n+1)] for _ in range(n+1)]

    for wire in wires:
        arr[wire[0]].append(wire[1])
        arr[wire[1]].append(wire[0])
        check[wire[0]][wire[1]] = True
        check[wire[1]][wire[0]] = True

    for i, wire in enumerate(wires):
        a,b = wire
        check[a][b] = False
        check[b][a] = False
        answer = min(answer, abs(BFS(n, a, arr, check) - BFS(n, b, arr, check)))
        check[a][b] = True
        check[b][a] = True

    return answer