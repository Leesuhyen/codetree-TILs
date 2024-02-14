n = int(input())


for i in range(n * 2):
    if i % 2 == 0:
        for k in range(n - (i//2)):
            print('*', end=' ')
        print()
    else:
        for j in range(i - (i//2)):
            print('*', end=' ')
        print()