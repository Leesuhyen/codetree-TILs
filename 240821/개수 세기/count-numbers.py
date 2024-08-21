qwe = list(map(int, input().split()))
num = list(map(int, input().split()))
cnt = 0
for i in range(qwe[0]):
    if qwe[1] == num[i]:
        cnt += 1
print(cnt)