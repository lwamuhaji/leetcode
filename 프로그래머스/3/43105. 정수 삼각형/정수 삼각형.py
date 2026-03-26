import copy

def solution(triangle):
    max_tri = copy.deepcopy(triangle)
    
    for i, row in enumerate(max_tri[:-1]):
        for j, n in enumerate(row):
            max_tri[i+1][j] = max(max_tri[i+1][j], triangle[i+1][j] + n)
            max_tri[i+1][j+1] = max(max_tri[i+1][j+1], triangle[i+1][j+1] + n)
    return(max(max_tri[-1]))