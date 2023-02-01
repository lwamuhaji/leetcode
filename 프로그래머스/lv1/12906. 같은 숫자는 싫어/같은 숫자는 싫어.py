def solution(arr):
    result = []
    temp = -1
    
    for n in arr:
        if temp != n:
            result.append(n)
            temp = n
    
    return result