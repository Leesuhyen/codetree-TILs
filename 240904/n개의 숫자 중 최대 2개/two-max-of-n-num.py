n = int(input())
num = list(map(int, input().split()))

max1 = 0
max2 = 0

  if num[0] > num[1]:
    max1 = num[0]
    max2 = num[1]
else:
    max1 = num[1]
    max2 = num[0]

for i in range(2, n):
    if max1 < num[i]: #max1이 num[i]보다 작을때
        max1 = max2
        max1 = num[i]
    elif max2 < num[1]:
        max2 = num[i]
print(max1, max2)