n = int(input())
k = 1
for i in range(n):
    for j in range(i +k):
        print('*', end='')
    k += 1
    print()