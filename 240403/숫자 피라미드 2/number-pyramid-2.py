n = int(input())

cnt = 1
for i in range(n):
    for j in range(1 + i):
        print(cnt, end=' ')
        cnt += 1
    print()