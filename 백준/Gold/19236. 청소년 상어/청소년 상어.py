import copy

# 8가지 방향 (↑, ↖, ←, ↙, ↓, ↘, →, ↗)
dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

def find_fish(board, fish_num):
    """특정 번호의 물고기 위치를 찾는 함수"""
    for i in range(4):
        for j in range(4):
            if board[i][j][0] == fish_num:
                return (i, j)
    return None

def move_all_fish(board, shark_x, shark_y):
    """1번부터 16번 물고기까지 순서대로 이동"""
    for i in range(1, 17):
        pos = find_fish(board, i)
        if pos is None: continue
        
        x, y = pos
        dist = board[x][y][1] # 현재 물고기 방향
        
        # 8방향 회전하며 이동 가능한지 확인
        for _ in range(8):
            nx, ny = x + dx[dist], y + dy[dist]
            if 0 <= nx < 4 and 0 <= ny < 4:
                if not (nx == shark_x and ny == shark_y): # 상어가 없는 곳
                    board[x][y][1] = dist # 확정된 방향 저장
                    board[x][y], board[nx][ny] = board[nx][ny], board[x][y]
                    break
            dist = (dist + 1) % 8

def get_shark_moves(board, shark_x, shark_y):
    """상어가 이동 가능한 모든 위치 반환"""
    moves = []
    dist = board[shark_x][shark_y][1]
    for i in range(1, 4): # 최대 3칸 이동 가능
        nx, ny = shark_x + dx[dist] * i, shark_y + dy[dist] * i
        if 0 <= nx < 4 and 0 <= ny < 4:
            if board[nx][ny][0] != -1: # 물고기가 있는 칸만
                moves.append((nx, ny))
        else:
            break
    return moves

max_score = 0

def solve(board, shark_x, shark_y, total):
    global max_score
    
    # 1. 보드 복사 (백트래킹을 위한 상태 저장)
    board = copy.deepcopy(board)
    
    # 2. 상어가 물고기를 먹음
    fish_num, fish_dist = board[shark_x][shark_y]
    total += fish_num
    board[shark_x][shark_y] = [-1, fish_dist] # 물고기 먹힘 표시
    
    max_score = max(max_score, total)
    
    # 3. 물고기 이동
    move_all_fish(board, shark_x, shark_y)
    
    # 4. 상어의 다음 이동 후보지 탐색
    possible_moves = get_shark_moves(board, shark_x, shark_y)
    
    # 5. 이동할 곳이 없으면 종료 (Base Case)
    if not possible_moves:
        return
    
    # 6. 재귀 호출 (Backtracking)
    for nx, ny in possible_moves:
        solve(board, nx, ny, total)

# 입력 처리
initial_board = [[None] * 4 for _ in range(4)]
for i in range(4):
    data = list(map(int, input().split()))
    for j in range(4):
        # 물고기 번호는 0부터 시작하도록 -1 해주거나, 
        # 방향 인덱스를 문제에 맞춰 조정 (문제는 1~8, 코드는 0~7)
        initial_board[i][j] = [data[j*2], data[j*2+1] - 1]

solve(initial_board, 0, 0, 0)
print(max_score)