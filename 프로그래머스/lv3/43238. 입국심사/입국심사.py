def solution(n, times):
    low, high = times[0], times[-1] * n
    mid = (low + high) // 2
    while (mid != high):
        if sum([mid//time for time in times]) < n:
            low = mid + 1
        else:
            high = mid
        mid = (low + high) // 2
    return mid