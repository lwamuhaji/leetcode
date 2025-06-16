N = int(input())
numbers = list(map(int, input().split()))

# Please write your code here.
even = len([_ for _ in numbers if _ % 2 == 0])
odd = N - even

answer = 0
flag = True
while True:
    if flag:
        if even > 0:
            even -= 1
            answer += 1
        elif odd >= 2:
            odd -= 2
            answer += 1
        elif odd == 1:
            answer -= 1
            break
        else:
            break
        flag = False
    else:
        if odd > 0:
            odd -= 1
            answer += 1
        else:
            break
        flag = True

print(answer)