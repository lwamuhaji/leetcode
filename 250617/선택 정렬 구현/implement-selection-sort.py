n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
for i in range(n):
    min = i
    for j in range(i+1, n):
        if arr[min] > arr[j]:
            min = j
    arr[min], arr[i] = arr[i], arr[min]

print(*arr)