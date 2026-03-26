# answer이 매우 작으므로 지도를 완성한다.
m = dict()

def foo(n):
    arr = m.get(n)
    for i in range(1, n//2 + 1):
        for a in m[i]:
            for b in m[n-i]:
                arr.add(a+b)
                arr.add(a-b)
                arr.add(b-a)
                if b != 0: arr.add(a/b)
                if a != 0: arr.add(b/a)
                arr.add(a*b)
    m[n] = arr
                
def solution(N, number):
    for i in range(1, 9):
        m[i] = {int(str(N)*i)}
        foo(i)
        if number in m[i]:
            return i
    return -1
    
    