def calc(list1, list2):
    result = set()
    for x in list1:
        for y in list2:
            result.add(x+y)
            result.add(x-y)
            result.add(x*y)
            if y != 0:
                result.add(x//y)
    return result

def solution(N, number):
    if N == number:
        return 1
    result = {}
    result[1] = {N}
    for n in range(2, 9):
        temp = set()
        temp.add(int(str(N) * n))
        for i in range(1, n):
            temp.update(calc(result[i], result[n-i]))
        if number in temp:
            return n
        result[n] = temp
    return -1