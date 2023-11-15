num = input().split()
a = int(num[0])
b = int(num[1])

if a < b:
    n = 1
else:
    n = 0

if b == a:
    m = 1
else:
    m = 0

print(n, end=' ')
print(m)