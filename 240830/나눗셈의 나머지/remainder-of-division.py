num = list(map(int,input().split()))
cnt_list = [0] * 7
n = 0
s = 0
while num[0] >= 1:
    n = num[0] % num[1]
    num[0] = num[0] // num[1]
    if n >= len(cnt_num):
        cnt_num.extend([0] * (n - len(cnt_num) + 1))
    cnt_list[n] += 1
for elem in cnt_list:
    s += elem * elem
print(s)