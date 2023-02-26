def union(parents, i, j):
    parents[max(find(parents, i), find(parents, j))] = min(find(parents, i), find(parents, j))
    
def find(parents, n):
    if parents[n] != n:
        return find(parents, parents[n])
    return n

def solution(n, computers):
    parents = [i for i in range(n)]
    answer = []
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                union(parents, i, j)
    for i in range(n):
        answer.append(find(parents, i))
    return len(set(answer))

def solution(n, computers):
    temp = []
    for i in range(n):
        temp.append(i)
    for i in range(n):
        for j in range(n):
            if computers[i][j]:
                for k in range(n):
                    if temp[k] == temp[i]:
                        temp[k] = temp[j]
    return len(set(temp))