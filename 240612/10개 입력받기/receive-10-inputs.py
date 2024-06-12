num = list(map(int, input().split()))
sum_val = 0
avg = 0
cnt = 0
for elem in num:
    if elem == 0:
        break
    cnt += 1
for i in range(cnt):
    sum_val += num[i]
avg = sum_val / cnt
print(f"{sum_val} {avg:.1f}")