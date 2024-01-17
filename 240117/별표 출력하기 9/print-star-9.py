n = int(input())

for k in range(n):
    for i in range(n - k - 1):
        print(' ', end=' ')
    for i in range(2 * k + 1):
        print('*', end=' ')
    print()