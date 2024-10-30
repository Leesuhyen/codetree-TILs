num = []
for i in range(10):
    num.append(input())
n = input()
cnt = 0
for i in range(10):
    if num[i][len(num[i]) -1] == n:
        print(num[i])
        cnt += 1
if cnt == 0:
    print('None')