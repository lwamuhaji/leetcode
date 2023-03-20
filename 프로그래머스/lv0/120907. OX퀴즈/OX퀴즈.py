def solution(quiz):
    return ['O' if eval(q.split("=")[0]) == eval(q.split("=")[1]) else 'X' for q in quiz]