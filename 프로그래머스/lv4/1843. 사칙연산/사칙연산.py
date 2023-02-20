memo = {}

def operate(arr, n):
    operator = arr[n]
    if operator == "+":
        result = arr[n - 1] + arr[n + 1]
    if operator == "-":
        result = arr[n - 1] - arr[n + 1]
    return arr[:n-1] + (result,) + arr[n+2:]

def foo(arr):
    if memo.get(arr):
        return memo[arr]
    results = []
    if len(arr) == 3:
        return operate(arr, 1)[0]
            
    for n in range(1, len(arr), 2):
        results.append(foo(operate(arr, n)))
    max_result = max(results)
    memo[arr] = max_result
    return max_result

def solution(arr):
    for i in range(0, len(arr), 2):
        arr[i] = int(arr[i])
        
    return foo(tuple(arr))
        