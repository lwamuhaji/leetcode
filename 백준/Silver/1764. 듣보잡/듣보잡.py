from sys import stdin
input = stdin.readline
N, M = map(int, input().strip().split())
S = sorted(list({input().strip() for _ in range(N)} & {input().strip() for _ in range(M)}))
print(len(S))
for s in S:
    print(s)
