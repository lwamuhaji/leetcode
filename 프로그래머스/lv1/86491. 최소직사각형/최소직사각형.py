def solution(sizes):
    for i in range(len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = [sizes[i][1], sizes[i][0]]
    w_max = max(sizes, key=lambda x:x[0])[0]
    h_max = max(sizes, key=lambda x:x[1])[1]
    return w_max * h_max
