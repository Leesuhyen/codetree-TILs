n = int(input())

for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(f"{i} * {j} = {i * j}", end=' ')
        if j % n == 0:
            print()
            n -= 1
        else:
            print("/", end=' ')