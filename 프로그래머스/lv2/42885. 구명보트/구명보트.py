from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    d = deque(people)
    while d:
        if d[0] + d[-1] > limit:
            answer += 1
            d.pop()
        else:
            answer += 1
            try:
                d.popleft()
                d.pop()
            except:
                ...
    return answer