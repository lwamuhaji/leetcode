

def count_connected(node, wires):
    pool = [node]
    i = 0
    while i < len(pool):
        for w in wires:
            if w[0] == pool[i] or w[1] == pool[i]:
                target = w[0] + w[1] - pool[i]
                if target not in pool:
                    pool.append(target)
        i += 1
    return len(pool)

def solution(n, wires):
    min_ = n
    for i in range(len(wires)):
        a = count_connected(wires[i][0], wires[:i] + wires[i+1:])
        b = count_connected(wires[i][1], wires[:i] + wires[i+1:])
        if abs(a - b) < min_:
            min_ = abs(a - b)
    return min_