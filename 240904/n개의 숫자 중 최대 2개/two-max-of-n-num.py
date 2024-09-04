n = int(input())
num = list(map(int, input().split()))

max1 = num[0]
max2 = num[1]

for i in range(n):
    if max1 < num[i]:
        max1 = max2
        max1 = num[i]
    elif max2 < num[i]:
        max2 = num[i]
print(max1, max2)