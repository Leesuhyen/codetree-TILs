n = int(input())

for i in range(n):
    for j in range(1 + i):
        print((i + 1) * (j + 1), end=' ')
    print()