N = int(input())
H = map(int, input().split())
W = map(int, input().split())

d = dict()
for h, w in zip(H, W):
    d[h] = d.get(h, 0) + w

current = 0
acc = 0
for h in range(200000, 0, -1):
    if h not in d: continue
    acc += d[h]
    if acc * h > current:
        current = acc * h
        
print(current)
    