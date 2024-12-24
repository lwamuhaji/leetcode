def marking(grid, points, route):
    time = 1 # 시작 시간
    r, c = points[route[0]-1] # 시작점
    grid[r][c].append(time) # (r, c) 마킹
    time += 1
    
    for point in route[1:]:
        nr, nc = points[point-1] # 목적지
        # (r + step, c) ~ (nr, c) 까지 마킹
        step = 1 if nr >= r else -1
        for i in range(r + step, nr + step, step):
            grid[i][c].append(time)
            time += 1
        # (nr, c + step) ~ (nr, nc) 까지 마킹
        step = 1 if nc >= c else -1
        for i in range(c + step, nc + step, step):
            grid[nr][i].append(time)
            time += 1
        r, c = nr, nc
            
def solution(points, routes):
    answer = 0
    grid = [[[] for _ in range(101)] for __ in range(101)]
    for route in routes:
        marking(grid, points, route)
        
    # 같은 공간에 같은 시간 감지
    for row in grid:
        for cell in row:
            visited = []
            for i, time in enumerate(cell):
                if time in visited:
                    continue
                visited.append(time)
                for other in cell[i+1:]:
                    if time == other:
                        answer += 1
                        break
    return answer