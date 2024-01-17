n = int(input())

for i in range(n):
    for k in range(i):
        print('  ', end='')

    for k in range((2 * n) - (2 * i) - 1):
        print('*', end=' ')
    print()