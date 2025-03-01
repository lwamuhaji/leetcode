N = int(input())
P = sorted(list(map(int, input().split())))
answer = 0
for i in range(N):
    answer += P[i] * (N-i)
print(answer)