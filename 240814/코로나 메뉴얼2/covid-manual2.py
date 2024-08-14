st = [0] * 5
for i in range(3):
    num = input().split()
    num[1] = int(num[1])
    if num[0] == 'Y':
        if num[1] > 36:
            st[0] += 1
        else:
            st[2] += 1
    else:
        if num[1] > 36:
            st[1] += 1
        else:
            st[3] += 1

if st[0] >= 2:
    sr = 'E'
print(f"{st[0]} {st[1]} {st[2]} {st[3]} {sr}")