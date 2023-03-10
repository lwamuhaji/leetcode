def solution(num, total):
    n = total/num - (num-1)/2
    return [n+i for i in range(num)]