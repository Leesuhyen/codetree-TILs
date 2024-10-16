n = int(input())
num = list(map(int, input().split()))
min_val = 1000
price = 0
max_p = 0
for i in range(n):
    for j in range(i + 1, n):
        price = num[j] - num[i]
        if price > max_p:
            max_p = price
print(max_p)