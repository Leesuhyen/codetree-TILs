num = list(map(int, input().split()))

max_val = 0
for i in range(len(num)):
    if max_val < num[i]:
        max_val = num[i]
print(max_val)