num = input().split()
c = num[0]
n = int(num[1])

if c =='A':
    for i in range(1, n + 1, 1):
        print(i, end=' ')
else:
    for i in range(n, 0, -1):
        print(i, end=' ')