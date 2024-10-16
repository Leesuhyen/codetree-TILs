n = int(input())
num = list(map(int, input().split()))
num_val = 0
min_val = 100
max_val = 0
for i in range(n):
    for j in range(i + 1, n):
        num_val = num[j] - num[i] 
        if num_val < min_val: 
            min_val = num_val
print(min_val)