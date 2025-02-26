import math
N = int(input())
SIZE = map(int, input().split())
T, P = map(int, input().split())

print(sum(map(lambda x: math.ceil(int(x)/T), SIZE)))
print(N//P, N%P)