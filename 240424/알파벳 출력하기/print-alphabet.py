n = int(input())
t = ord('A')
for i in range(n):
    for j in range(i + 1):
        print(chr(t), end='')
        t += 1
    print()