num = list(map(int, input().split()))
s_num = 0
r_num = 0
cnt = 0
for elem in num[1::2]:
    s_num += elem

for  elem in num[2::3]:
    r_num += elem
    cnt += 1
t_num = r_num // cnt
print(f"{s_num} {t_num:.1f}")