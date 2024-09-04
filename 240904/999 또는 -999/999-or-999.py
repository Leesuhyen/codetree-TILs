num = list(map(int, input().split()))

max_val = num[0]
min_val = num[0]
for i in range(len(num) - 1):
    if max_val > num[i]:
        max_val = num[i]
    if min_val < num[i]:
        min_val = num[i]

print(min_val, max_val)