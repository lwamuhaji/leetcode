from collections import deque

adjs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def solution(maps):
    visited = [[0 for x in range(len(maps[0]))] for y in range(len(maps))]
    depths = [[0 for x in range(len(maps[0]))] for y in range(len(maps))]
    queue = deque([(0,0)])
    
    while queue:
        current = queue.popleft()
        visited[current[0]][current[1]] = 1
        
        for x, y in adjs:
            next_x = current[0] + x
            next_y = current[1] + y
            if next_x >= 0 and next_y >= 0 and next_x < len(maps) and next_y < len(maps[0]) and maps[next_x][next_y] and not visited[next_x][next_y]:
                depths[next_x][next_y] = depths[current[0]][current[1]] + 1
                queue.append((next_x, next_y))
    answer = depths[len(maps)-1][len(maps[0])-1]
    if answer == 0:
        return -1
    return answer + 1