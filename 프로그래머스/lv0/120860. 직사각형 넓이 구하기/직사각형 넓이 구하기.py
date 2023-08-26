def solution(dots):
    x1, y1 = dots[0]
    x2, y2 = dots[1]
    x3, y3 = dots[2]
    x4, y4 = dots[3]
    if x1 == x2:
        return abs(y1-y2) * abs(x1-x3)
    elif x1 == x3:
        return abs(y1-y3) * abs(x1-x2)
    elif x1 == x4:
        return abs(y1-y4) * abs(x1-x2)