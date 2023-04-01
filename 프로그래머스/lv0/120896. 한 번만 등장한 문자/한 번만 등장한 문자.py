def solution(s):
    myList = [0 for _ in range(26)]
    answer = ''
    for char in s:
        myList[ord(char) - 97] += 1
    for i, n in enumerate(myList):
        if n == 1:
            answer += chr(i + 97)
    return answer