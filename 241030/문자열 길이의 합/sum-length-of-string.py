n = int(input())
num = []
cnt = 0
total = 0
for i in range(n):
    num.append(input())
for k in range(n):
    total += len(num[k])
    if num[k][0] == 'a':
        cnt += 1
print(total, cnt)