num = list(map(int, input().split()))

n = len(num)
s = 0
for i in range(n):
    if num[i] == 0:
        s = i
        break
t = num[s-1] + num[s-2] + num[s-3]
print(t)