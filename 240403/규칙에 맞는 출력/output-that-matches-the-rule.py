n = int(input())

for i in range(n):
    for j in range(1 + i):
        print((n - i) + j, end=' ')
    print()