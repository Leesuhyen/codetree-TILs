num = list(map(int, input().split()))
min_val = 1000
max_val = 1

for i in range(len(num)):
    if min_val > num[i] and num[i] > 500:
        min_val = num[i]
    if max_val < num[i] and num[i] < 500:
        max_val = num[i]
print(max_val, min_val)