n = input().split()
a = int(n[0])
b = int(n[1])

for i in range(a, 9, 2):
    for j in range(b, a - 1, - 1):
        print(f"{j} * {i} = {j * i}", end=' ')
        if j != a:
            print('/', end=' ')
    print()