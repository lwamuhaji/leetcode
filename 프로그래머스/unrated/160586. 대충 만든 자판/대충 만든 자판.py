def solution(keymap, targets):
    d = {}
    for keys in keymap:
        for i, key in enumerate(keys):
            d[key] = i + 1 if i + 1 < d.get(key, 101) else d[key]
    
    answer = []
    for target in targets:
        n = 0
        f = False
        for c in target:
            if c not in d:
                answer.append(-1)
                f=True
                break
            n += d[c]
        if f:
            continue
                
        answer.append(n)
    return answer
            
            