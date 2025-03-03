N = int(input())
for i in range(N):
    k = i
    s = i
    while i:
        n = i%10
        i //= 10
        s += n
    if s == N:
        print(k)
        break
else:
    print(0)