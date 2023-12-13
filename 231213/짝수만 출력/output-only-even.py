num = input().split()

a = int(num[0])
b = int(num[1])


while a <= b:
    print(a, end=' ')
    a += 2

'''
for i in range(a, b + 1, 2):
    print(i, end=' ')
'''