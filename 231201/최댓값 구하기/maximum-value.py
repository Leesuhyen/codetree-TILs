num = input().split()
a = int(num[0])
b = int(num[1])
c = int(num[2])



if a > b:
    if b > c:
        print(a)
    elif a < c:
        print(c)
    else:
        print(a)
else:
    if b > c:
        print(b)
    else:
        print(c)