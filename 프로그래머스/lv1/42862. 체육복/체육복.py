def solution(n, lost, reserve):
    for k in set(lost) & set(reserve):
        lost.remove(k)
        reserve.remove(k)
    
    lost.sort()
    reserve.sort()
    
    cnt = 0
    for l in lost:
        for r in reserve:
            if abs(l - r) == 1:
                reserve.remove(r)
                cnt += 1
                break
    return n - len(lost) + cnt