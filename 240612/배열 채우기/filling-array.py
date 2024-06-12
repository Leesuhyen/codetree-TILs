num = list(map(int, input().split()))
cnt = -1
for elem in num:
    if elem == 0:
        break
    cnt += 1   
for i in range(cnt, -1, -1):
    print(num[i], end=' ')