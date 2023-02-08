def solution(n, lost, reserve):
    '''
    [마지막 제한사항 대응]
    집합으로 만들어서 lost와 reserve의 교집합을 구하고 각각 뺀다.
    '''
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