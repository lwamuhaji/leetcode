from sys import stdin

N, M = map(int, input().split())
S = sorted(list({input() for _ in range(N)} & {input() for _ in range(M)}))
print(len(S))
for s in S:
    print(s)
