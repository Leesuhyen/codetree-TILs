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

#for elem in st:
   # print(elem, end=' ')
for j in range(len(st) -1):
    print(st[j], end=' ')
if st[0] >= 2:
    print('E')