n = int(input())
num = list(map(int, input().split()))
min_val = num[0]
cnt = 0
for i in range(len(num)):
    if min_val > num[i]:
        min_val = num[i]
for elem in num:
    if elem == min_val:
        cnt += 1
print(min_val, cnt)