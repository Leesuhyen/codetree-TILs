n = int(input())

for i in range(n):
    cnt = 0
    num = input().split()
    a = int(num[0])
    b = int(num[1])
    for j in range(a, b + 1):
        if j % 2 == 0:
            cnt += j
    print(cnt)