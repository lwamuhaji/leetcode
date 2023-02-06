def solution(number, k):
    answer = ''
    while True:
        for n in range(int(max(number)), 0, -1):
            if (index := number.find(str(n))) == -1:
                continue
            if index < k:
                answer += str(n)
                number = number[index+1:]
                k = k - index
                break
            if index == k:
                answer += number[index:]
                return answer

def solution(number, k):
    stack = []
    for n in number:
        while stack and stack[-1] < n and k > 0:
            stack.pop()
            k -= 1
        stack.append(n)
    if k != 0:
        return ''.join(stack)[:-k]
    return ''.join(stack)
    