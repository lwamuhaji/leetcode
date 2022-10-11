class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        s = s.lstrip()
        if not s:
            return 0
        if s[0] == '+' or s[0] == '-':
            sign = 1 if s[0] == '+' else -1
            s = s[1:]
            index = len(s)
            for i, c in enumerate(s):
                if not c.isdigit():
                    index = i
                    break
        else:
            index = len(s)
            for i, c in enumerate(s):
                if not c.isdigit():
                    index = i
                    break
                    
        print(s[:index])
        num = (0 if s[:index] == '' else int(s[:index])) * sign
        if num > 2**31 - 1:
            num = 2**31 -1
        if num < -2**31:
            num = -2**31
        return num
            