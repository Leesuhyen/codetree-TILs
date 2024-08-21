st = [0] * 5
for i in range(3):
    num = input().split()
    num[1] = int(num[1])
    if num[0] == 'Y' and num[1] >= 37:
        st[0] += 1
    elif num[0] == 'N' and num[1] >= 37:
        st[1] += 1
    elif num[0] == 'Y' and num[1] <= 37:
        st[2] += 1
    else:
        st[3] += 1

if st[0] >= 2:
    sr = 'E'
    print(f"{st[0]} {st[1]} {st[2]} {st[3]} {sr}")