def solution(game_board, table):
    length = len(game_board)
    
    def visit_board(x, y, routes):
        visited[x][y] = True
        routes.append((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if not (nx < length and nx >= 0 and ny < length and ny >= 0):
                continue
            if not visited[nx][ny] and game_board[nx][ny] == 0:
                visit_board(nx, ny, routes)
        return routes
    
    def visit_table(x, y, routes):
        visited[x][y] = True
        routes.append((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx = x + dx
            ny = y + dy
            if not (nx < length and nx >= 0 and ny < length and ny >= 0):
                continue
            if not visited[nx][ny] and table[nx][ny] == 1:
                visit_table(nx, ny, routes)
        return routes
    
    def to_matrix(block):
        x_list = [node[0] for node in block]
        y_list = [node[1] for node in block]
        
        min_x = min(x_list)
        max_x = max(x_list)
        x_len = max_x - min_x + 1
        
        min_y = min(y_list)
        max_y = max(y_list)
        y_len = max_y - min_y + 1
        
        matrix = [[0 for x in range(x_len)] for y in range(y_len)]
        
        for x, y in block:
            matrix[y - min_y][x - min_x] = 1
        return matrix
    
    def is_fit(block, empty_space):
        if len(block) != len(empty_space):
            return False
        
        block_matrix = to_matrix(block)
        empty_space_matrix = to_matrix(empty_space)
        
        for _ in range(4):
            if block_matrix == empty_space_matrix:
                return True
            block_matrix = [list(l) for l in zip(*block_matrix[::-1])]
        return False
        
    empty_spaces = []
    visited = [[False for i in range(length)] for j in range(length)]
    for x in range(length):
        for y in range(length):
            if not visited[x][y] and game_board[x][y] == 0:
                empty_spaces.append(visit_board(x, y, []))
    
    blocks = []
    visited = [[False for i in range(length)] for j in range(length)]
    for x in range(length):
        for y in range(length):
            if not visited[x][y] and table[x][y] == 1:
                blocks.append(visit_table(x, y, []))
    
    answer = 0
    for block in blocks:
        for empty_space in empty_spaces:
            if is_fit(block, empty_space):
                empty_spaces.remove(empty_space)
                answer += len(block)
                break
                
    return answer