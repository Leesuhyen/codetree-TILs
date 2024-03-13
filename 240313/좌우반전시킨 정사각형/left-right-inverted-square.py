n = int(input())

for i in range(n):
    for j in range(n):
        print(n - j + n*i - i*j, end=' ')
    print()

'''
for i in range(1, n+1):
    for j in range(n):
        print((n-j)*i, end=' ')
    print()
'''