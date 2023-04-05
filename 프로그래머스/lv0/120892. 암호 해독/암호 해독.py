def solution(cipher, code):
    return ''.join([c for i, c in enumerate(cipher) if i%code==code-1])