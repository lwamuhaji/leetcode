def solution(s, n):
    answer = ''
    for c in s:
        if c == ' ':
            answer += c
        elif ord(c) >= 97:
            answer += chr(((ord(c) - 97) + n) % 26 + 97)
        elif ord(c) < 97:
            print(((ord(c) - 65) + n) % 26 + 65)
            answer += chr(((ord(c) - 65) + n) % 26 + 65)
    return answer
            