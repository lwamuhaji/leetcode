str = input()

# Please write your code here.
stack = []
for c in str:
    if c == '(':
        stack.append(c)
    else:
        if stack:
            stack.pop()
        else:
            break
else:
    if stack:
        print("No")
    else:
        print("Yes")
    exit()

print("No")

