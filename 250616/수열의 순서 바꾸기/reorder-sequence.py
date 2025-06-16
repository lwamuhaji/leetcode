n = int(input())
sequence = list(map(int, input().split()))

# Please write your code here.
pos = 0
for i in range(len(sequence)-1):
    if sequence[i] > sequence[i+1]:
        pos = i + 1
print(pos)