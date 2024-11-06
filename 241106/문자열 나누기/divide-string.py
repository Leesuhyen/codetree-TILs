n = int(input())
num = input().replace(' ', '')
cnt = 0

for i in range(len(num)):
    if (i + 1) % 5 == 0:
        print(num[i])
    else:
        print(num[i], end='')