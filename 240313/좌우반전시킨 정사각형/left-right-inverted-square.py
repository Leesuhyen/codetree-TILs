n = int(input())

for i in range(n):
    for j in range(n):
        print(n - j + n*i - i*j, end=' ')
    print()