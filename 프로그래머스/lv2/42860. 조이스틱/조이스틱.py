visited = [False for _ in range(20)]
cost = 0
answers = []
length = 0

def dfs(targets, position):
    global visited, cost
    isLeaf = True
    for t in targets:
        if not visited[t]:
            isLeaf = False
            temp = visited[:]
            temp_cost = cost
            cost += min(abs(position - t), length - abs(position - t))
            visited[t] = True
            dfs(targets, t)
            visited = temp
            cost = temp_cost
    if isLeaf:
        answers.append(cost)

def solution(name):
    global length
    
    length = len(name)
    # 방문할 글자의 위치를 초기화한다.
    targets = [i for i, char in enumerate(name) if char != 'A']
    
    a = 0
    for char in name:
        diff = ord(char) - ord('A')
        moves = min(diff, 26-diff)
        a += moves
    
    dfs(targets, 0)
    return min(answers) + a
    
    