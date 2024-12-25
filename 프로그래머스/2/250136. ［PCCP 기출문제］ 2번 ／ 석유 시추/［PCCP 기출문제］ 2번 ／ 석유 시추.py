def add_adj(queue, x, y, w, h):
    if x + 1 < h:
        queue.append([x + 1, y])
    if y + 1 < w:
        queue.append([x, y + 1])
    if x - 1 >= 0:
        queue.append([x - 1, y])
    if y - 1 >= 0:
        queue.append([x, y - 1])

def solution(land):
    height, width = len(land), len(land[0])
    
    # 지도 그리기
    for x, row in enumerate(land):
        for y, n in enumerate(row):
            if n == 1:
                # BFS START
                found = []
                queue = []
                add_adj(queue, x, y, width, height)
                while queue:
                    cx, cy = queue.pop(0)
                    if land[cx][cy] == 0:
                        continue
                    elif land[cx][cy] == 1:
                        land[cx][cy] = 0
                        found.append([cx, cy])
                        add_adj(queue, cx, cy, width, height)
                # BFS END
                
                # MARKING
                marked = {}
                for fx, fy in found:
                    if fy not in marked:
                        land[fx][fy] = len(found)
                        marked[fy] = fx
                    elif marked[fy] > fx:
                        land[marked[fy]][fy] = 0
                        land[fx][fy] = len(found)
                        marked[fy] = fx
    
    for row in land[1:]:
        for i in range(len(row)):
            land[0][i] += row[i]
    return max(land[0])

def solution(land):
    n, m = len(land), len(land[0])
    visited = [[True]*m for _ in range(n)]
    delta = [(1,0),(-1,0),(0,1),(0,-1)]
    oil_cnt = [0]*m
    for i in range(n):
        for j in range(m):
            if land[i][j] and visited[i][j]:
                visited[i][j] = False
                s = [(i,j)]
                col = set()
                oil = 0
                while s:
                    x, y = s.pop()
                    col.add(y)
                    oil += 1
                    for dx, dy in delta:
                        X, Y = x+dx, y+dy
                        if 0<=X<n and 0<=Y<m and land[X][Y] and visited[X][Y]:
                            visited[X][Y] = False
                            s.append((X,Y))
                for y in col:
                    oil_cnt[y] += oil
    return max(oil_cnt)
                
                    