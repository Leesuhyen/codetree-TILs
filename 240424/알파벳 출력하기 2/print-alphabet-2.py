n = int(input())

t = ord('A')

for i in range(n):
    for j in range(i):
        print(' ', end=' ')
    for j in range(n - i):
        print(chr(t), end=' ')
        t += 1
    print()