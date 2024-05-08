n = int(input())


p = 0

for i in range(n):
    num = input().split()
    a = int(num[0])
    b = int(num[1])
    for j in range(a, b + 1):
        p += j
    print()