arr = input().split()
a = int(arr[0])
b = int(arr[1])
t = 0
'''
if a < b:
    if a % 2 == 0:
        while a <= b:
            print(b, end=' ')
            b -= 2
    else:
        while t <= b:
            print(b, end=' ')
            b -= 2
else:
    if a % 2 == 0:
        while b <= a:
            print(a, end=' ')
            a -= 2
    else: 
        while t <= b:
            print(b, end=' ')
            b -= 2        
'''



if a < b:
    t = a
    a = b
    b = t

while a >= b:
    if a % 2 == 0:
        print(a, end=' ')
        a -= 1
    else:
        a -= 1