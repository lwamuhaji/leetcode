n, m = map(int, input().split())
arr = list(map(int, input().split()))

# Please write your code here.
answer = 0
pos = 0
while(pos < n):
    if arr[pos]:
        pos += 2 * m + 1
        answer += 1
    else:
        pos += 1
print(answer)