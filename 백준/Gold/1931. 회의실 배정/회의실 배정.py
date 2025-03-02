from sys import stdin
input = stdin.readline
N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]
meetings = sorted(meetings, key=lambda x: (x[1], x[0]))

now, cnt = 0, 0
for start, end in meetings:
    if now <= start:
        cnt += 1
        now = end
print(cnt)