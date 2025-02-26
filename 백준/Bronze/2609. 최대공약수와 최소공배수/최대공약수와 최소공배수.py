a, b = map(int, input().split())
mul = a*b
while b:
    a, b = b, a%b
print(a)
print(int(mul/a))