def solution(chicken):
    answer = 0
    n = chicken
    while n >= 10:
        answer += n // 10
        n = n % 10 + n // 10
    return answer