def solution(triangle):
    line1 = [{triangle[0][0]}]
    
    for _ in range(len(triangle)-1):
        temp = []
        for _ in range(len(line1)+1):
            temp.append(set())
        for i, numbers in enumerate(line1):
            for n in numbers:
                temp[i].update({triangle[len(line1)][i] + n})
                temp[i] = {max(temp[i])}
                temp[i+1].update({triangle[len(line1)][i+1] + n})
                temp[i+1] = {max(temp[i+1])}
        line1 = temp
    result = set()
    
    for s in line1:
        result.update(s)
        
    return max(result)