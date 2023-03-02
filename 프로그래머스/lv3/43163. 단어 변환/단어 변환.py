

def solution(begin, target, words):
    length = len(words[0])
    words.insert(0, begin)
    queue = [0]
    visited = [False for n in range(len(words))]
    visited[0] = True
    
    depths = [0 for n in range(len(words))]
    
    while queue:
        current = queue.pop(0)
        for next in range(len(words)):
            if visited[next]:
                continue
            diff = 0
            for i in range(length):
                if words[next][i] != words[current][i]:
                    diff += 1
            if diff == 1:
                depths[next] = depths[current] + 1
                if words[next] == target:
                    return depths[next]
                visited[next] = True
                queue.append(next)
    return 0
        