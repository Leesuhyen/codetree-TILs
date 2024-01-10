n = int(input())

for k in range(n):
    for i in range(n-k):
        for j in range(n-k):
            print('*', end='')
        print(end=' ')    
    print()