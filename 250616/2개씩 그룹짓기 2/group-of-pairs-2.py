n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
arr.sort()
k = int(len(arr)/2)
answer = 1000000000
for i in range(k):
    answer = answer if answer < (arr[i+k] - arr[i]) else arr[i+k] - arr[i]
print(answer)