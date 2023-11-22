num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

s_num = b if b < c else c

if s_num == a:
    print(1, end = " ")
else:
    print(0, end = " ")

if a == b == c:
    print(1)
else:
    print(0)