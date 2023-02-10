def solution(s):
    if len(s) == 4 or len(s) == 6:
        for c in s:
            if c.isalpha():
                return False
        return True
    return False