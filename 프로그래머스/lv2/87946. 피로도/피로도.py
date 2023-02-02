def solution(k, dungeons):
    return len(dungeons) - _solution(k, dungeons)

def _solution(k, dungeons):
    r = [_solution(k - d[1], dungeons[:i] + dungeons[i+1:]) for i, d in enumerate(dungeons) if k >= d[0]]
    if len(r) == 0:
        return len(dungeons)
    else:
        return min(r)