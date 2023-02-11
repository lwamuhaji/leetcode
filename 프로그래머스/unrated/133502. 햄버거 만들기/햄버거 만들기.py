def solution(ingredient):
    stack = []
    answer = 0
    for i in ingredient:
        stack.append(i)
        if stack[-4:] == [1,2,3,1]:
            answer += 1
            [stack.pop() for _ in range(4)]
    return answer