import math

def solution(n):
    for i in range(math.ceil(math.sqrt(n)) + 1):
        if n == i**2:
            return 1
    return 2