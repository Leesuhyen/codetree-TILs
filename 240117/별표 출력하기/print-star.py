n = int(input())


for i in range(n):
    for k in range(1 + i):
        print('*', end=' ')
    print()
for j in range(n - 1):
    j += 1
    for k in range(n - j):
        print('*', end=' ')
    print()