n = int(input())

for i in range(n):
    for k in range(n - i):
        print('*', end=' ')
    print()
for i in range(n - 1):
    for k in range(2 + i):

        print('*', end=' ')
    print()