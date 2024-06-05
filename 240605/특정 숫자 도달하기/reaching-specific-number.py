arr = list(map(int, input().split()))

sum_val = 0
sum_avg = 0
cnt = 0
for elem in arr:
    if elem >= 250:
        break
    sum_val += elem
    cnt += 1
sum_avg = sum_val/cnt
print(sum_val, sum_avg)