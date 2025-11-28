import sys
input = sys.stdin.readline
print = sys.stdout.write
T = int(input().rstrip())
for _ in range(T):
    a, b = map(int, input().rstrip().split())
    print(str(a+b)+"\n")