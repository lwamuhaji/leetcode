from sys import stdin
input = stdin.readline
M = int(input())
s = set()
for _ in range(M):
    op = input().split()
    if op[0] == 'all':
        s = {i for i in range(1, 21)}
    elif op[0] == 'empty':
        s = set()
    elif op[0] == 'add':
        s.add(int(op[1]))
    elif op[0] == 'remove':
        if int(op[1]) in s:
            s.remove(int(op[1]))
    elif op[0] == 'check':        
        print(1) if int(op[1]) in s else print(0)
    elif op[0] == 'toggle':      
        s.remove(int(op[1])) if int(op[1]) in s else s.add(int(op[1]))