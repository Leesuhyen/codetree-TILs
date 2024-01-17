n = int(input())

for i in range(n):
    for k in range(n - i):
        print('*', end='')
    for k in range(2 * i):
        print(' ', end='')
    for k in range(n - i):
        print('*', end='')
    print()

'''
for i in range(n):
    for k in range(i + 1):
        print('*', end='')
    for k in range((n * 2) - (i * 2) - 2):
        print(' ', end='')
    for k in range(i + 1):
        print('*', end='')
    print()
'''