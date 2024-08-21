num = list(map(int,input().split()))
cnt_list = [0] * 7
n = 0
s = 0
while num[0] >= 1:
    n = num[0] % num[1]
    num[0] = num[0] // num[1]
    cnt_list[n] += 1
for elem in cnt_list:
    s += elem * elem
print(s)