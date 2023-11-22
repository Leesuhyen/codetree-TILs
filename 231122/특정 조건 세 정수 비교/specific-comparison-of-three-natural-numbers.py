num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])

s_num = a if a <= b and a <= c else b

if s_num == a:
    print(1, end = " ")
else:
    print(0, end = " ")

if a == b and b == c:
    print(1)
else:
    print(0)