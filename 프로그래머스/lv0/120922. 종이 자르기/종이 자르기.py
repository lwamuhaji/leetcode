def solution(M, N):
    return max(M, N) - 1 + (min(M, N) - 1) * max(M, N)