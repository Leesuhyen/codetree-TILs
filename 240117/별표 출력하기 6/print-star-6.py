n = int(input())

for i in range(n):
    for k in range(i):
        print('  ', end='')

    for k in range((2 * n) - (2 * i) - 1):
        print('*', end=' ')
    print()
for k in range(n - 1):
    k += 1
    for i in range(n - k - 1):
        print(' ', end=' ')
    for i in range(2 * k + 1):
        print('*', end=' ')
    print()