max_memo = [[None for _ in range(201)] for __ in range(201)]
min_memo = [[None for _ in range(201)] for __ in range(201)]

def foo(arr, start, end):
    if max_memo[start][end] != None:
        return max_memo[start][end], min_memo[start][end]
    
    if start == end:
        return int(arr[start]), int(arr[start])
    
    results = []
    for n in range(0, end - start, 2):
        a = foo(arr, start, start + n)
        b = foo(arr, start + n + 2, end)
        if arr[start + n + 1] == "+":
            results.append(a[0] + b[0])
            results.append(a[1] + b[1])
        elif arr[start + n + 1] == "-":
            results.append(a[0] - b[1])
            results.append(a[1] - b[0])
    
    max_memo[start][end] = max(results)
    min_memo[start][end] = min(results)
    return max(results), min(results)

def solution(arr):
    return foo(arr, 0, len(arr)-1)[0]