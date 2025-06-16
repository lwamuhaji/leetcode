N = int(input())

command = []
num = []

for _ in range(N):
    line = input().split()
    command.append(line[0])
    if line[0] == "push_back" or line[0] == "get":
        num.append(int(line[1]))
    else:
        num.append(0)

# Please write your code here.
myList = []
while command:
    c, n = command.pop(0), num.pop(0)
    if c == 'push_back':
        myList.append(n)
    elif c == 'pop_back':
        myList.pop()
    elif c == 'get':
        print(myList[n-1])
    else:
        print(len(myList))