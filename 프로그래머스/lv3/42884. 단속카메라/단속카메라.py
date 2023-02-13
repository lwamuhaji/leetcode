def solution(routes):
    routes.sort(key=lambda x: x[1])
    answer = 0
    i = 0
    while i < len(routes):
        n = 1
        while i+n < len(routes) and routes[i][1] >= routes[i+n][0]:
            n += 1
        i += n
        answer += 1
    return answer
        
    