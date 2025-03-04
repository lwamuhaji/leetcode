N, r, c = map(int, input().split())

left, right = 0, 2**N - 1
low, high = 0, 2**N - 1
quadrants = []

for _ in range(N):
    hm, vm = (left+right)//2, (low+high)//2
    hf, vf = False, False
    
    if c <= hm:
        hf = True
        right = hm
    else:
        left = hm+1
    if r <= vm:
        vf = True
        high = vm
    else:
        low = vm+1
        
    if hf and vf:
        quadrants.append(0)
    elif not hf and vf:
        quadrants.append(1)
    elif hf and not vf:
        quadrants.append(2)
    else:
        quadrants.append(3)
        
answer = 0 
for i, q in enumerate(quadrants):
    answer += q * 4**(N-i-1)
print(answer)