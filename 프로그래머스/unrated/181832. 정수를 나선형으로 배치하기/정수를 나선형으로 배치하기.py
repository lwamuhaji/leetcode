def solution(n):
    x, y = 0, 0
    answer = [[0 for _ in range(n)] for __ in range(n)]
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    d = 0
    for i in range(n**2):
        answer[y][x] = i + 1
        x += directions[d%4][0]
        y += directions[d%4][1]
        if not (0 <= x < n and 0 <= y < n) or answer[y][x] != 0:
            x -= directions[d%4][0]
            y -= directions[d%4][1]
            d += 1
            x += directions[d%4][0]
            y += directions[d%4][1]
    return answer