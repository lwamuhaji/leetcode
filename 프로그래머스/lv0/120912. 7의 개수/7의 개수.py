def solution(array):
    answer = 0
    for num in array:
        while num:
            n = num % 10
            if n == 7:
                answer += 1  
            num = num // 10
    return answer