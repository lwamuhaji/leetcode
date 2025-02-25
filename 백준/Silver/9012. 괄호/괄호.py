n = int(input())
for _ in range(n):
    stack = []
    string = input()
    for c in string:
        if c == '(':
            stack.append(0)
        elif stack:
            stack.pop()
        else:
            print("NO")
            break
    else:
        if not stack:
            print("YES")
        else:
            print("NO")