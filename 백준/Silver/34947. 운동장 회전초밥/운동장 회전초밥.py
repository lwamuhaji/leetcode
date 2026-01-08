import math

N, T = map(int, input().split())
R, D, θ, W = map(int, input().split())
W = W/100

def distance(r):
    l = 2*r*math.cos(θ*math.pi/180/2)+D
    return 2*math.pi*r*θ/360*2+2*l

정민 = distance(R-(3*W)+(1/2)*W) * N / T
정화 = distance(R-(3*W)+(3/2)*W) * N / T
은체 = distance(R-(3*W)+(5/2)*W) * N / T

print(은체 - 정민)
print(은체 - 정화)