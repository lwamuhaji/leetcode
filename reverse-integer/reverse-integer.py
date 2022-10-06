class Solution:
    def reverse(self, x: int) -> int:
        stack = []
        answer = 0
        flag = -1 if x < 0 else 1
        x = x if x >= 0 else -x
        
        while x > 0:
            stack.append(x % 10)
            x = x // 10
        
        print(stack)
        
        n = 1
        while stack:
            answer += stack.pop() * n
            n = n * 10
        
        answer = answer * flag
            
        return answer if answer <= 2**31-1 and answer >= -2**31 else 0