def solution(targets):
    targets = sorted(targets, key=lambda x: x[1])
    count, end = 0, 0
    for target in targets:
        if target[0] >= end:
            end = target[1]
            count += 1
    return count
    
        
        