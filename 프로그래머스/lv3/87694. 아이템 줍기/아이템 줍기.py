MAX_SIZE = 500
diffs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def is_onside(node, rect):
    x, y = node
    if ((x == rect[0] or x == rect[2]) and (y >= rect[1] and y <= rect[3])) or ((y == rect[1] or y == rect[3]) and (x >= rect[0] and x <= rect[2])):
        return True
    return False

def is_inside(node, rect):
    x, y = node
    if (x < rect[2] and x > rect[0]) and (y < rect[3] and y > rect[1]):
        return True
    return False

def adjacencies(node, rectangle):
    x, y = node
    target = []
    result = []
    for rect in rectangle:
        if is_onside(node, rect):
            target.append(rect)
    
    ban = []
    for dx, dy in diffs:
        nx = x + dx
        ny = y + dy
        for rect in target:
            if x == rect[0] and (y != rect[1] and y != rect[3]):
                if is_onside((nx, ny), rect) and (nx == rect[2]):
                    print('here', rect, x, y)
                    ban.append((nx, ny))
            elif x == rect[2] and (y != rect[1] and y != rect[3]):
                if is_onside((nx, ny), rect) and (nx == rect[0]):
                    ban.append((nx, ny))
            elif y == rect[1] and (x != rect[0] and x != rect[2]):
                if is_onside((nx, ny), rect) and (ny == rect[3]):
                    ban.append((nx, ny))
            elif y == rect[3] and (x != rect[0] and x != rect[2]):
                if is_onside((nx, ny), rect) and (ny == rect[1]):
                    ban.append((nx, ny))
            if is_onside((nx, ny), rect):
                result.append((nx, ny))
    
    result = list(set(result))
    for node in ban:
        result.remove(node)
    
    inside = []
    for nx, ny in result:
        for rect in target:
            if is_inside((nx, ny), rect):
                inside.append((nx, ny))
    
    for node in inside:
        result.remove(node)
    
    return result
    

def solution(rectangle, characterX, characterY, itemX, itemY):
    queue = [(characterX, characterY)]
    visited = [[False for x in range(MAX_SIZE)] for y in range(MAX_SIZE)]
    depths = [[0 for x in range(MAX_SIZE)] for y in range(MAX_SIZE)]

    while queue:
        current_node = queue.pop(0)
        x, y = current_node
        visited[x][y] = True

        for next_node in adjacencies(current_node, rectangle):
            nx, ny = next_node
            if visited[nx][ny]:
                continue
            depths[nx][ny] = depths[x][y] + 1
            queue.append(next_node)
            
    return depths[itemX][itemY]