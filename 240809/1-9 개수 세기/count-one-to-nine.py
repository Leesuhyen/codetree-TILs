n = int(input())

num = list(map(int, input().split()))

for i in range(1, 10):
    cnt = 0
    for elem in num:
        if elem == i:
            cnt += 1

    print(cnt)