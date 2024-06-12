n = int(input())
arr = list(map(float,input().split()))

sum_val = 0
sum_avg = 0
for elem in arr:
    sum_val += elem
sum_avg = sum_val / n
print(f"{sum_avg:.1f}")
if sum_avg >= 4.0:
    print('Perfect')
elif sum_avg >= 3.0:
    print('Good')
else:
    print('Poor')